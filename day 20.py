#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
s_val = 0
for q in range(n):
    i=0
    while i<n-1:
        x=a[i]
        y=a[i+1]
        
        if x>y:
            a[i]=y
            a[i+1]=x
            s_val += 1
        else:
            pass
        i+=1
print("Array is sorted in {} swaps.".format(s_val))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n-1]))
