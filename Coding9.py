# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:52:51 2019

@author: Pratik
"""

str1 = ""
str2 = "prats"
#list[<start>:<stop>:<step>]
inp=[1,2,3,4,5,6,7,8,9]

def bin_search(a,left,right,key):
    if(left>right):
        return False
    else:
        mid=int((left+right)/2)
        if(key==a[mid]):
            return True
        elif(key>a[mid]):
           return bin_search(a,mid+1,right,key)
        else:
           return bin_search(a,left,mid-1,key)


def check_palin(ip):
    temp=""
    for i in ip[::-1]:
        temp=temp+i
    
    print(temp)
    if temp==ip:
        return True
    return False

print(bin_search(inp,0,len(inp)-1,12))



if check_palin(str1):
    print("YES")
else:
    print("NO")
    
