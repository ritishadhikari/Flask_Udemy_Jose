# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:53:18 2019

@author: ritis
"""

def func():
    print("Func() in one.py")
    
print("Top Level in one.py")

if __name__ == "__main__":
    print("One.py is being run directly")
else :
    print("One.py has been imported")
