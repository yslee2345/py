# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:25:31 2017

@author: stu
"""

class Car(object):
    def __init__(self):
        self.max_speed =160
        self.speed=0;
    
    def speed_up(self):
        if self.speed<=140:
            self.speed+=20
        else:
            print("NO")
            
    def speed_down(self):
        if self.speed>=20:
            self.speed-=20
        else:
            print("NO")
a=Car()
a.speed_up()
print(a.speed)
a.speed_down()
print(a.speed)

class SportsCar(Car):
    def __init__(self):
        super(SportsCar,self).__init__()
        self.max_speed=200
    def speed_up(self):
        if self.speed<=155:
            self.speed+=45
        else:
            print("NO")
    def speed_down(self):
        if self.speed(self)>=45:
            self.speed+=45
        else:
            print("NO")
            
class Truck(Car):
    def __init__(self):
        super(Truck,self).__init__()
        self.max_speed=100
    def speed_up(self):
        if self.speed<=85:
            self.speed+=15
        else:
            print("NO")
    def speed_down(self):
        if self.speed(self)>=15:
            self.speed-=15
        else:
            print("NO")
            
            
a=SportsCar()
a.speed_up()
b=Truck()
b.speed_up()
print(b.speed)            
            

class Complex(object):
    
    def __init__(self,realpart,imagpart):
        self.realpart = realpart
        self.imagpart = imagpart
        
    
c=complex(1,2)
print(c)
    
class Complex2(Complex):
    def __repr__(self):
        return "Complex : real = %f imag  = %f" % (self.r,self.i)
    
    def __str__(self):
        return "[for str]" + self.__repr__()
    
c2= Complex2(1,1)
print(c2)
    
    
import numpy as np
a=np.array([0,1,2,3,4,5,6,7,8,9])   
b=[]
for ai in a:
    b.append(ai*2)
c=a*2       
    
a=np.array([1,2,3])
b=np.array([10,20,30]) 
2*a+b  
    
b=np.array([[0,1,2],[3,4,5]])
len(b)
len(b[0])

c=np.array([[10,20,30],[40,50,60]])

a=np.array([[1,2],[3,4]])
b=np.array([[4,3],[2,1]])
c=a*b

import numpy as np   
a=np.array([0,1,2,3,4,5,6,7,8,9])
idx = np.array([True, False, True, False, True, False, True, False, True, False])
a[idx]
a[a%2==0] 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    