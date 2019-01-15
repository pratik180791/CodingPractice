# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 14:31:46 2018

@author: Pratik
"""

a = [7,6,12,3,9,3,5,1,12]


tem={}
#print(a)
b=[]
target = 10
res=0
for i in range(len(a)):
    diff = target-a[i]
    
    if diff in a and diff not in tem.values() and a[i]!=diff:
                tem[diff] = a[i]
                res+=1
 
print(len(tem.keys()))
print(tem)