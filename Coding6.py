# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:29:27 2019

@author: Pratik
"""

bill=[3,10,2,9]
ana=1
bill_charged=7
combined_bill=0




for i in range(len(bill)):
    if i==ana:
        pass
    else:
        combined_bill+=bill[i]        

diff=bill_charged-(combined_bill/2)

if diff==0:
    print("Bon Appetit")
else:
    print(int(diff))