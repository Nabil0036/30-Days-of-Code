#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    

    i=0
    summ=[]
    while i<4:
        j=0
        while j<4:
            t00=arr[0+i][0+j]
            t01=arr[0+i][1+j]
            t02=arr[0+i][2+j]
            t10=arr[1+i][0+j]
            t11=arr[1+i][1+j]
            t12=arr[1+i][2+j]
            t20=arr[2+i][0+j]
            t21=arr[2+i][1+j]
            t22=arr[2+i][2+j]
            a=1
            b=1
            c=1
            d=0
            e=1
            f=0
            g=1
            h=1
            ii=1
            t00*=a
            t01*=b
            t02*=c
            t10*=d
            t11*=e
            t12*=f
            t20*=g
            t21*=h
            t22*=ii
            temp=(t00+t01+t02+t10+t11+t12+t20+t21+t22)
            summ.append(temp)
            j+=1
        i+=1
    print(max(summ))
