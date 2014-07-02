/*Write a program that reads a file containing a sorted list of words 
(one word per line, no spaces, all lower case), then identifies the longest
word in the file that can be constructed by concatenating copies of
shorter words also found in the file. 

For example, if the file contained: 
       cat
       cats
       catsdogcats
       catxdogcatsrat
       dog
       dogcatsdog
       hippopotamuses
       rat
       ratcatdogcat 

The answer would be 'ratcatdogcat' - at 12 letters, it is the longest
word made up of other words in the list.  The program should then
go on to report how many of the words in the list can be constructed
of other words in the list. */

/* @file.main.cpp @brief @auther viva FUNG*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <stack>
#include <Trie.h>

class LookAheadBuffer{
  public:
    LookAheadBuffer(ITrie* trie = NULL, int i = 0)
      :savedTrie(trie), savedI(i){}

    void get(ITrie*& trie, int& i) const {
     trie = savedTrie;
     i = savedI;
    }

    ITrie* savedTrie;
    int savedI;
};

typedef std::stack<LookAheadBuffer> LookAheadContextStack;
/*nTrie to be used for look ahead in the given string str.
 * Upon return this parameter holds Trie for first character after found word*
 * str[in] to be look ahead for words. [in /out ] for the location within string parameter str from 
 * where the look ahead is to be started.*/

bool lookAhead(ITrie* nTrie, const std::string& str, int& from, const int to, LookAheadContextStack& context){
  int i = from;
  ITrie* nTrieNext = nTrie->Next(str[i++]);
  ITrie* peekAhead = nTrieNext;
  while(peekAhead && !peekAhead->isEmpty() && i < to){
    peekAhead = peekAhead->Next(str[i++]);
  }

  if(peekAhead == NULL){
    return false;}

  else if(peekAhead->isEmpty()){                                                                                                                       
    context.push(LookAheadBuffer(nTrie,i));                                                                                                            
    i = from;                                                                                                                                          
    nTrie = peekAhead;                                                                                                                                 
    return true;                                                                                                                                       
  }                                                                                                                                                    
  return false;                                                                                                                                        
}                                                                                                                                                      
                                                                                                                                                       
int main(int argc, char* argv[])                                                                                                                       
{                                                                                                                                                      
  const char* WordsFile = (argc == 2)? argv[1] : "problemwords.txt";                                                                                   
  std::fstream wordStream(WordsFile);                                                                                                                  
  std::istream_iterator<std::string> itr_word(wordStream), itr_word_end;                                                                               
  ITrie* trie[26] = {0};                                                                                                                               
  for(int i = 0; i<26; ++i){                                                                                                                           
    //Totally 26 different Trie Tree for 26 alphabetes                                                                                                 
    trie[i] = new Trie();                                                                                                                              
    }                                                                                                                                                  
                                                                                                                                                       
  typedef std::list<std::list> StringList;                                                                                                             
  typedef std::map<unsigned int, StringList> LengToStringMap;                                                                                          
  typedef std::set<int> SetOfLength;                                                                                                                   
  LengToStringMap lengthStringMap;                                                                                                                     
  //map for grouping strings based on their length                                                                                                     
  SetOfLength lengthSet;                                                                                                                               
  //set of lengths of all strings in the file                                                                                                          
                                                                                                                                                       
 unsigned int numWords = 0;                                                                                                                            
 std::cout << "Loading string from file" << WordsFile << std::endl;                                                                                    
 for( ; itr_word != itr_word_end; ++itr_word, ++numwords){                                                                                             
   const unsigned index = tolower(itr_word->at(0)) - 'a';                                                                                              
   //Get the trie index ofr the string                                                                                                                 
                                                                                                                                                       
   trie[index] = trie[index]->Add(*itr_word);                                                                                                          
   //Add the string the trie                                                                                                                           
   const size_t wordLength = itr_word->length();                                                                                                       
   lengthStringMap[wordLength].push_back(*itr_word);                                                                                                   
   //put the string in its length group                                                                                                                
   lengthSet.insert(wordLength);          
 //put the length of string to the set                                                                                                               
   }                                                                                                                                                   
                                                                                                                                                       
std::cout << "String loaded" << std::endl;                                                                                                             
const char* FoundWordsFile = "words_found.txt";                                                                                                        
std::ofstream logFile(FoundWordsFile);                                                                                                                 
int numStringFound = 0;                                                                                                                                
                                                                                                                                                       
//Iterate over set of lengths beginning with longest length                                                                                            
for(SetOfLengths::reverse_iterator itr = lengthSet.rbegin(); itr != lengthSet.rend(); itr++){                                                          
  const size_t stringLength = *itr;                                                                                                                    
  const StringList& sl = lengthStringMap[stringLength];                                                                                                
                                                                                                                                                       
for(StringList::const_iterator sitr = sl.begin(); sitr != sl.end(); sitr++){                                                                           
  ITrie* nTrie = trie[tolower((*sitr[0]) - 'a')];                                                                                                      
  //get the correct trie for the string                                                                                                                
  int i = 0;                                                                                                                                           
  bool wordFound = false, isLookedAhead = false, fromContext = false;                                                                                  
                                                                                                                                                       
  LookAheadContextStack lookAheadContext;                                                                                                              
  while(i <= stringLength){                                                                                                                            
    //Iterate over string                                                                                                                              
    while(nTrie && !nTrie->isEmpty() && i < stringLength){                                                                                             
      //Iterate until a word is found                                                                                                                  
      nTrie = nTrie->Next(*sitr[i++]);                                                                                                                 
    }                                                                                                                                                  
  if(stringLength == i || nTrie == NULL){                                                                                                              
    if(wordFound && nTrie && nTrie->isEmpty()){                                                                                                        
      //if iteration ends iwth finding word then break                                                                                                 
      break;                                                                                                                                           
      }                                                                                                                                                
    if(isLookAhead){                                                                                                                                   
      //reached end because of lookahead then backtrack to previous context                                                                            
      lookAheadContext.top().get(nTrie, i);                                                                                                            
      //get the last lookahead context from top                                                                                                        
      lookAheadContext.pop();                                                                                                                          
      //pop off the last context                                                                                                                       
      fromContext = true;                                                                                                                              
    }                                                                                                                                                  
    if(lookAheadContext.empty()){              
    //all lookahead contexts have been searched now                                                                                                    
    isLookedAhead = false;                                                                                                                             
    }                                                                                                                                                  
    continue;                                                                                                                                          
  }                                                                                                                                                    
  break;                                                                                                                                               
  }                                                                                                                                                    
//look ahead only if we are not backtracking when fromContext is false                                                                                 
if(!fromContext && lookAhead(nTrie, *sitr, i, stringLength, lookAheadContext)){                                                                        
  isLookedAhead = true;                                                                                                                                
  continue;                                                                                                                                            
}                                                                                                                                                      
  fromContext = false;          //enable look aheads;                                                                                                  
  nTrie = trie[tolower((*sitr)[i]) - 'a'];    //switch the trie to next word's first character                                                         
  wordFound = true;     //a word is found                                                                                                              
}                                                                                                                                                      
                                                                                                                                                       
//Desired string is found only if iteration is complete with wordFound set and Trie is empty                                                           
if(wordFound && i == stringLength && nTrie && nTrie->isEmpty()){                                                                                       
  ++numStringFound;                                                                                                                                    
  if(1 == numStringFound)                                                                                                                              
  {                                                                                                                                                    
    std::cout << "longest string is : " << *sitr << endl;                                                                                              
    std::cout << "Finding other strings... " << endl;                                                                                                  
  }                                                                                                                                                    
                                                                                                                                                       
  logFile << *sitr << "\n";                                                                                                                            
}                                                                                                                                                      
}                                                                                                                                                      
  if(numStringFound){std::cout << ".";}                                                                                                                
  //clean up the trie                                                                                                                                  
  for(int i = 0; i < 26; ++i)                                                                                                                          
  {                                                                                                                                                    
    delete trie[i];                                                                                                                                    
    trie[i] = NULL;                                                                                                                                    
  }                                                                                                                                                    
  logfile.close();                                                                                                                                     
  std::cout << "\nNumber of words composed of other words in the list: " << numStringFound << "\n" << "Total number of words read: " <<                
  numWords << "\n" << "Words found are saved in file: " << FoundWordsFile << endl;                                                                     
  return 0;                                                                                                                                            
}                                                                                                                                                      
                                   
