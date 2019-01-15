# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:46:41 2018

@author: Pratik
"""

import threading
class Sample:
    
    def __init__(self):
        self.var_1 = 1
        self.var_2 = "TEST"
    
    
    def func_print(self, var):
        print(self.var_2," ")
        print(var)
      
    def func_square(self,var):
        try:
            print(var**2)
        except:
            print("EXCEPTION ALERT")

    
    
    
s =  Sample()
s.func_print("PT")



"""
thread.start_new_thread(s.func_print("PT"))
thread.start_new_thread(s.func_square(76))
"""

if __name__ == "__main__":
    t1 = threading.Thread(target=s.func_print, args=("PRATS",))
    t2 = threading.Thread(target=s.func_square, args=(9,))
    t3 = threading.Thread(target= lambda a,b : print(a**b), args=(9,3,))
#print(s.func_square(2))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()

        