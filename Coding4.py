# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 00:15:31 2019

@author: Pratik
"""

data=[1,2,4,5,4,3,2,1,3,4]

res={}
cnt=1
for i in range(0,len(data),1):
    if data[i] in res.keys():
        print(res)
        temp=res[data[i]]
        res[data[i]]=temp+1
    else:
        print(res)
        res[data[i]]=cnt

max1=0
max_key=0
for key,val in res.items():
    if val>max1:
        max1=val
        if key<max_key and max_key!=0:
            max_key=key
        else:
            max_key=key
            
print(max_key)        
#return max1