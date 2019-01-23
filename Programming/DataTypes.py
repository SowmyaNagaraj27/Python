#!/usr/bin/env python3

import platform

print('This is python version {}'.format(platform.python_version()))

def main():
    message()
    
def message():
    print ("this is a function. def represents function")
    print('line2')
    
# this line forces interpreter to read the entire script before it executes the code
if __name__ == '__main__': main()
   

#Using format

x = 42
print('hello, value of x is {}'.format(x))

#Everything is an object in python, here string is an object so print calls the object
s='hello, value of x is {}'.format(x)
print(s)

#using fstring
print(f'hello, value of x is {x}')

#blocks and indents
x=10
y=12

if x<y:
    print('x is greater than y')
else:
    print('y is greater')

print('outside the block')

z=112
if x<z:
    print(f'z= {z}')
    print('line 1')
    
print('outside')

#conditions

x=71
if x ==5:
    print(f'{x}')
elif x == 7:
    print(f'{x}')
else:
    print ('do something else')

#Class and objects
class Duck:
    sound = 'Quack'
    walk = 'Walking like a duck'
    
    def quack(self):
        print('Quack')
        
    def walka(self):
        print(self.walk)

def main():
    donald = Duck()
    donald.quack()
    donald.walka() 

if __name__ == '__main__': main()     

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:29:39 2019

@author: Sowmya
"""
x=True
print(type(x))

x=7>5
print('{}'.format(x))  

x=None
print('{}'.format(x)) 

#Lists
x =[1,2,23,4,5]
x[1] = 12
for i in x:
    print('i is {}'.format(i))

#tuples - Immutable
x=(1,2,3,4,5)
for i in x:
    print('i in {}'.format(i))
    
#sequence with range
x=range(1,10)
for i in x:
    print('i is {}'.format(i))
    
#id
x=23
y=23
print(id(x))
print(id(y))

#Loops
secret = "asdfghjkl"
pw=""

while pw!= secret:
    pw = input('what is the secret word?')


x=range(10,100,10)
for i in x:
    print(f'{i}')

#functions
def main():
    x=kitten()
    print(f'{x}')

def kitten():
    return 'Meow'

if __name__ == '__main__': main() #used to import modules

##default
def main():
    kitten1(1,2)

def kitten1(a,b,c=0):
    print('a, b, c: {},{},{}'.format(a,b,c))
    return 'Meow'

if __name__ == '__main__': main()   
 
#Function by args
def main():
    #kitten2('hi', 'hello', 'how are you')
    x=('hi', 'hello', 'how are you')
    kitten2(*x)
    
def kitten2(*args):
     if len(args):
         for i in args:
             print(i)
     else:
         print('nothing passed')
if __name__=='__main__': main()

#keyword arguments or dictionary 
def main():
    #kitten3(cat='Meow', dog='bark')
    x=dict(cat='Meow', dog='bark')
    kitten3(**x)

def kitten3(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('{} say {}'.format(k, kwargs[k]))
    else:
        print('nothin in x')

if __name__=='__main__': main()
