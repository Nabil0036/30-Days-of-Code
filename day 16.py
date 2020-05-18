#!/bin/python3

import sys


S = input().strip()
try:
    q=int(S)
    print(q)
except Exception as e:
    print('Bad String')
