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
    
    #Class Object Attributes - Everything is going to be true regardless of the instances of the class
    
    species = 'mammal'
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        
x = Dog(breed='lab', name= 'sam')


print(type(x))
print(x.breed)
print(x.name)
print(x.species)



class Circle:
    
    def __init__(self, radius=1):
        self.radius = radius
        self.pi = 3.14
        
    def area(self):
        return self.radius*self.radius*self.pi
    
    def circumference(self):
        return int(self.pi*2*self.radius)
        
mycircle = Circle(radius=10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumference())


class animal():
    def __init__(self, fur):
        print('Animal Created')
        self.fur = fur
        
    def report (self):
        print('Animal')
        
    def eat(self):
        print('Eating!')
        
a = animal(fur='Oily')
a.eat()
a.report()


class dog(animal):
    def __init__(self,fur):
        animal.__init__(self,fur)
        print('Dog Created!')
    
    def report (self):
        print('Dog Reporting')
        
d = dog(fur = 'fuzzy')

d.eat()

d.report()


class book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
            
    def __len__(self):
        return self.pages
    
    def __repr__(self):
        return f"Title : {self.title}, Author : {self.author}"
        
mybook = book(title='Python', author='Ritish', pages=250)

print(mybook)
print(len(mybook))