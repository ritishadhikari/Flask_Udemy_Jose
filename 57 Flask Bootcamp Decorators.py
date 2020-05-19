# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:21:31 2019

@author: ritis
"""
#1
def hello():
    print('Hello')

hello()

#2  Function inside a function
def hello(name = 'Ritish'):
    print('the hello() func has been run')
    
    def greet():
        return " This is inside the greet() "
    
    print(greet())
    
    def welcome():
        return " This is inside welcome() "
    
    print(welcome())

hello()


#3 Returning Functions
def hello(name = 'Ritish'):
    print('the hello() func has been run')
    
    def greet():
        return " This is inside the greet() "
    
    def welcome():
        return " This is inside welcome() "
    
    if name == 'Ritish':
        return greet
    else:
        return welcome

x = hello(name='Sammy')
print(x())


#4 Functions as Arguments

def hello():
    return 'Hi Jose'

def other (func):
    print ("Some other code")
    print(func())
    
other(func=hello)



def hello():
    return 'Hi Jose'

def other (func):
    print ("Some other code")
    return func() + ' how are You'
    
x = other(func=hello)
x




def hello(m = 'Hi Jose'):
    return m

def other (func):
    print ("Some other code")
    return func() + ' how are You'
    
x = other(func=hello)
x



#5 creating a decorator
def new_decorator(func):
    
    def wrap_func():
        print("Some code before executing func")
        
        func()
        
        print("Code here, after executing func()")
    
    return wrap_func

def func_needs_decorator():
    print("Please Decorate me!!")


func_needs_decorator = new_decorator(func=func_needs_decorator)

func_needs_decorator()

# The same thing as 5
@new_decorator
def func_needs_decorator():
    print("Please Decorate me!!")
func_needs_decorator()  


#example
def other (func):
    print ("Some other code")
    return func() + ' how are You'

@other
def hello(m = 'Hi Jose'):
    return m

hello


def other (func):
    
    def wrap_func():
        
        #print ("Some other code")
        
        return func() + ' how are You'
    
    return wrap_func

@other
def hello(m = 'Hi Jose'):
    return m

hello()


#example

def new_decorator(func):
    
    def wrap_func():
        return func() - 4.5
    return wrap_func

@new_decorator
def area_rectangle():
    return 5*5

area_rectangle()

#------------------------------------------------------------------------------------

def new_decorator(func):
    
    def wrap_func(a,b,rule):
        if rule == 'add':     
            return func(a,b,rule) + 4.5
        else:
            return func(a,b,rule) - 4.5 
    return wrap_func

@new_decorator
def area_rectangle(a,b,rule):
    return a*b

area_rectangle(a= 5, b = 6, rule='sub')