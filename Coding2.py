# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:07:19 2019

@author: Pratik
"""

def isprime(num):
    if(num<=1): 
        return False
    for i in (2,num-1):
        if(num%2==0 or num%3==0 or num%5==0):
            #print(i)
            return False
    return True

def calc_prime_factor(num):
    #print(num)
    for i in range(1,num):
        #print(i)
        if(num%i==0):
            if(isprime(i)):
                print(i)
                    

    
if __name__=="__main__":
    calc_prime_factor(600851475143)
    