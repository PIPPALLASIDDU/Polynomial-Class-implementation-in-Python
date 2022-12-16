from os import *
from sys import *
from collections import *
from math import *

from copy import deepcopy

class Polynomial:

    def __init__(self):
        self.degCoeff=[]

    def copy_const(self,obj):
        self.degCoeff=obj.copy()

    def setCoefficient(self,ind,val):
        arr=self.degCoeff
        if len(arr)==0:
            for i in range(ind+1):
                arr.append(0)
        if ind<=len(arr)-1:
            arr[ind]=val
        else:
            rn=ind-(len(arr)-1)
            for i in range(rn+1):
                arr.append(0)
            arr[ind]=val
    def print(self):
        arr=self.degCoeff
        for i in range(len(arr)):
            if arr[i]!=0:
                print("{}x{}".format(arr[i],i),end=" ")
    
    def __add__(self,o):
        res=Polynomial()
        arr1=self.degCoeff
        arr2=o.degCoeff
        i,j=0,0
        while i<len(arr2) and i<len(arr1):
            res.setCoefficient(i, arr1[i]+arr2[i])
            i+=1
        while i<len(arr1):
            res.setCoefficient(i, arr1[i])
            i+=1
        while i<len(arr2):
            res.setCoefficient(i, arr2[i])
            i+=1
        return res
    def __sub__(self,o):
        res=Polynomial()
        arr1=self.degCoeff
        arr2=o.degCoeff
        i=0
        while i<len(arr2) and i<len(arr1):
            res.setCoefficient(i, arr1[i]-arr2[i])
            i+=1
        while i<len(arr1):
            res.setCoefficient(i, arr1[i])
            i+=1
        while i<len(arr2):
            res.setCoefficient(i, -arr2[i])
            i+=1
        return res
    
    def __mul__(self,o):
        res=Polynomial()
        arr2=(o.degCoeff)
        arr1=self.degCoeff
        for i in range(len(arr1)):
            if arr1[i]!=0:
                arr2=deepcopy((o.degCoeff))
                for j in range(len(arr2)):
                    arr2[j]*=arr1[i]
                for k in range(i):
                    arr2.insert(0,0)
                x=Polynomial()
                x.copy_const(arr2)
                res=res+x
        return res

def run():
    count1 = int(input())

    degree1 = list(map(int,input().split()))

    coeff1 = list(map(int,input().split()))


    first = Polynomial()
    for i in range(count1):
        first.setCoefficient(degree1[i], coeff1[i])


    count2 = int(input())


    degree2 = list(map(int,input().split()))

    coeff2 = list(map(int,input().split()))


    second = Polynomial()
    for i in range(count2) :
        second.setCoefficient(degree2[i], coeff2[i])


    choice = int(input())
 
    result = Polynomial()
    # Add 
    if choice == 1:
        result = first + second
        result.print()
    # Subtract
    elif choice == 2:
        result = first - second
        result.print()
    # Multiply
    elif choice == 3:
        result = first * second
        result.print()

    elif choice == 4: # Copy constructor
        third = deepcopy(first)
        if (third.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")

    else: # Copy assignment operator
        fourth = deepcopy(first)
        if (fourth.degCoeff == first.degCoeff) :
            print("true")
        else :
            print("false")

run()
