/* @file TrieChildren.h represented a TRIE with 26 children*/

#ifndef _TRIECHILDREN_H_
#define _TRIECHILDREN_H_

#include "ITrie.h"
#include <string>

#define NUM_CHARS 26
class TrieChildren: public ITrie{
  public:
      //Brief Constructor
      TrieChildren(const char lable, ITrie* child, const std::string& word, const bool storeEmpty);
      virtual ITrie* Add(const std::string& word);
      virtual ITrie* Next(const char ch);
      virtual bool Empty() const;

  private:
      virtual ~TrieChildren();
      TrieChildren(const TrieChildren&);
      TrieChildren& operator=(const TrieChildren& rhs);

  private:
      bool _isEmpty_;
      ITrie* children_[NUM_CHARS];
};

#endif /*_TRIECHILDREN_H_*/

==================================================================

/* @file TrieChildren.cpp to implement Trie Tree*/

#include <ctype.h>
#include <string.h>
#include "TrieChildren.h"
#include "Trie.h"

TrieChildren::TrieChildren(const char lable, ITrie* child, const std::string& word, const bool storeEmpty)
  :_isEmpty_(storeEmpty)
  {
    memset(children_, 0, sizeof(children_));
    children_[tolower(lable) - 'a'] = child;
    Trie t;
    children_[tolower(word[0]) - 'a'] = t.Add(word.substr(1));
}

ITrie* TrieChildren::Add(const std::string& word){
  if("" == word){
    _isEmpty_ = true;
    return this;
  }

  const unsigned childINDEX = tolower(word[0]) - 'a';
  if(children_[childINDEX]){
  children_[childINDEX] = children_[childINDEX]->Add(word.substr(1));
  }

  else{
    Trie t;
    children_[childINDEX] = t.Add(word.substr(1));
    return this;
  }
}

ITrie* TrieChildren::Next(const char ch){
  char lowerCH = tolower(ch);
  return (lowerCH >= 'a' && lowerCH <= 'z')? children_[lowerCH - 'a']:NULL;

}

bool TrieChildren::Empty() const {
  return _isEmpty_;

}

TrieChildren::~TrieChildren(){                                                                                                                         
  for(int i = 0; i < NUM_CHARS; ++i){                                                                                                                  
    if(children_[i]){                                                                                                                                  
      delete children_[i];                                                                                                                             
      children_[i] = NULL;                                                                                                                             
    }
  }
}

