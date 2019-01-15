# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:42:18 2019

@author: Pratik
"""

#ip=[10,20,20,10,10,30,50,10,20]
ip=[1,1,3,1,2,1,3,3,3,3]
de=['a','b','c','d','b']
re=[0]*256

for i in range(len(de)):
    #print(ord(de[i]))
    if re[ord(de[i])]==0:
        re[ord(de[i])]=1
    elif re[ord(de[i])]==1:
        print("Duplicate")
        print(de[i])
    else:
        pass
    
pairs={}
for i in ip:
    if i in pairs.keys():
        temp=pairs[i]
        pairs[i]=temp+1
        
    else:
        pairs[i]=1


total_pairs=0
for key,value in pairs.items():
    if value%2==0:
        total_pairs+=value/2       
    else:
        if (value-1)%2==0:
            print(value-1)
            total_pairs+=(value-1)/2
            
print(int(total_pairs))