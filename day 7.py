#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    l = len(arr)
    inv_arr=[]
    i=1
    while i<=n:
        a=arr[-i]
        inv_arr.append(a)
        i+=1
    
    for j in inv_arr:
        print(j,end=" ")
