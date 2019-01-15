# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:58:52 2019

@author: Pratik


security qa team
security features
bots/malicious attacks
verify features/find bugs
details/implementation 
"""

def func_consec_Add(input_array):
        output={}
        op=[]
        fl=False
        input_array.append(-1)
        for i in range(len(input_array)): 
            
         
            temp=input_array[i]
            if(i==0):
                continue
            
            while(i>0 and input_array[i]==input_array[i-1]):
                temp=temp+input_array[i-1]
                output[input_array[i]]=temp
                i=i+1
                print(i,input_array[i])
            
            print(input_array[i],temp)
            output[input_array[i]]=temp
              
            """     
            if i<len(input_array)-1:
                while(input_array[i]==input_array[i+1]):
                    temp=temp+input_array[i]
                    print(i)
                    i=i+1
                    print(i)
                           
                    #print(temp)
            """
              
        output.pop(-1)
        print(output)
        
input_ar=[1,1,2,2,2,3,5,5,6,6]
func_consec_Add(input_ar)