# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:54:19 2019

@author: Pratik
"""
import json
temp = {"USD":[{"INR":70},{"CAD":0.9}],
"INR":[{"USD":0.14}]
}

data = json.dumps(temp)
processed_j = json.loads(data)

#1 3 2 6 1 2
"""
data=[1,3,2,6,1,2]
k=3
#print(len(data))


count=0
result1=[]
for i in range(len(data)-1,0,-1):
    for j in range(len(data)-2,-1,-1):
        if(i==j):
            pass
        else:
            if data[i]<data[j]:
                if((data[i]+data[j])%k==0):
                    result1.append(str(data[i])+""+str(data[j]))
                    print(data[i],data[j])

for i in range(len(data)):
    for j in range(i+1,len(data)):
        #pass
        print(data[i],data[j])
    
        if(j<len(data)):
            if data[i]<data[j]:
                if((data[i]+data[j])%k==0):
                    result1.append(str(i)+""+str(j))
                    print(data[i],data[j])
                    
print(count)
print(result1)
"""
    #for l in range(len(data)-1,0):
        #print(data[k],data[l])


def prc_search(ip,op):
    tp=0
  
    for key,val in processed_j.items():
        if key == ip:
            #print("KEY FOUND")
            for i in val:
                for ky,vl in i.items():
                    if(ky == op):
                        #print("VAL FOUND")
                        #print(ky,vl)
                        tp=vl
                        return tp
                    else:
                        #pass
                            prc_search(op,ip)
                        
                    return tp      #print(val) 





print(prc_search("INR","USD"))
