
/* @file Trie.h @brief class that represent a Trie with no children*/                     
#ifndef _TRIE_H_
#define _TRIE_H_
                                                                                          
#include "ITrie.h"
#include <string> 

class Trie : public ITrie{                                                                
  public:
    Trie(const bool E = false)                                                            
      :_isEmpty_(E){}
    virtual ITrie* Add(const std::string& word);
    virtual ITrie* Next(const char ch);
    virtual bool Empty() const;
    virtual ~Trie(){}

  private:
    bool _isEmpty_;
};
#endif

===============================================================
#include "Trie.h"
#include "TrieChild.h"
#include <string>

ITrie* Trie::Add(const std::string& word){
  return (word == "")?  (ITrie*) new Trie(true): (ITrie*) new TrieChild(word, _isEmpty_);
}

ITrie* Trie::Next(const char ch){return NULL;}

bool Trie::Empty() const {return _isEmpty_;}


