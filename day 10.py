#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = format(n,"b")
    #print(binary)
    k=0
    li=[]
    for i in binary:
        if i == '1':
            k+=1
            #print(k)
        elif i == '0':
            li.append(k)
            k=0
    li.append(k)
    m = max(li)
    print(m)
