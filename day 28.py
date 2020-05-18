#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    fnames = []
    eids = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if str(emailID).endswith("@gmail.com"):
            fnames.append(firstName)
            eids.append(emailID)
    names= sorted(fnames)
    for n in names:
        print(n)
