# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 23:24:57 2019

@author: Pratik
"""

lbs = [100,90,90,80,75,60] #[100,100,50,40,40,20,10]
#100 90 90 80 75 60
alic = [50, 65, 77, 90, 102]#[5,25,50,120]
#[50 65 77 90 102]
lb=sorted(set(lbs),reverse=True)
ranks = {}
alic_rank={}
for i in range(len(lb)):
    ranks[lb[i]]=i+1
 
min_rank=min(lb)
max_rank=max(lb)
final_res=[]
for i in range(len(alic)):
        if(alic[i]>max_rank):
            alic_rank[alic[i]]=1
            max_rank=alic[i]
        elif(alic[i]<min_rank):
            
            alic_rank[alic[i]]=ranks[min_rank]+1
            min_rank=alic[i]
        else:
            for key in ranks.keys():
                if(alic[i]<key):
                    continue
                elif(alic[i]>key):
                     alic_rank[alic[i]]=ranks[key]
                     print(alic[i],ranks[key],alic_rank[alic[i]])
                     break
                elif(alic[i]==key):
                    #print("Hello",ranks[key],alic[i],ranks[key])
                    alic_rank[alic[i]]=ranks[key]
                    #print(alic[i],ranks[key])
                    break
                else:
                    continue

print(alic_rank)
for key,val in alic_rank.items():
    print(val)

         
            