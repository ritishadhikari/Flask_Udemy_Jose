# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:28:02 2019

@author: ritis
"""

class Sample():
    pass

x = Sample()

print(type(x))


class Dog():
    
    def __init__(self, breed):
        self.breed = breed
        
x = Dog(breed='lab')

print(type(x))
