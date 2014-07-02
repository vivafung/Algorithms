#ifndef __ITRIE_H__
#define __ITRIE_H__

#include<string>
class ITrie
{
public:
virtual ITrie* Add(const std::string& word) = 0;
virtual ITrie* Next(const char ch) = 0;
virtual bool IsEmpty() const = 0;
virtual ~ITrie() {}
};

#endif 
