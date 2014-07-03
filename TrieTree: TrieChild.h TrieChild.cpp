/* @file TrieChild.h, represent a TRIE with one child */

#ifndef _TRIECHILD_H_
#define _TRIECHILD_H_

#include "ITrie.h"

class TrieChild : public ITrie{
  public:
  //Brief Constructor
    TrieChild(const std::string& word, const bool storeEmpty);

    virtual ITrie* Add(const std::string& word);
    virtual ITrie* Next(const char ch);
    virtual bool Empty() const;

  private:
    virtual ~TrieChild();
    TrieChild(const TrieChild&);
    TrieChild& operator=(const TrieChild& rhs);

  private:
    bool _isEmpty_;
    char _lable_;
    ITrie* _child_;
};
#endif

===========================================================
/* @file TrieChild.cpp to implement the class TrieChild*/

#include "TrieChild.h"
#include "Trie.h"
#include "TrieChildren.h"
#include <ctype.h>

TrieChild::TrieChild(const std::string& word, const bool storeEmpty)
  :_isEmpty_(storeEmpty),_lable_(tolower(word[0]))
{
  Trie t;
  _child_ = t.Add(word.substr(1));
}

ITrie* TrieChild::Add(const std::string& word){
  if(word == ""){
  _isEmpty_ = true;
  return this;
  }

  if(_lable_ == tolower(word[0])){
  _child_ = _child_->Add(word.substr(1));
  return this;
  }

  return new TrieChildren(_lable_,_child_,word,_isEmpty_);
}

ITrie* TrieChild::Next(const char ch){
  return (tolower(ch) == _lable_)? _child_ : NULL;
}

bool TrieChild::Empty() const{
  return _isEmpty_;
}

TrieChild::~TrieChild(){
  if(_child_){
    delete _child_;
    _child_ = NULL;
  }
}
