# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
n = int(input())
li = []
for _ in range(n):
    k = int(input())
    h = math.sqrt(k)
    if k>3:
        for i in range(2,int(h)+1):
            g= True
            if k%i == 0:
                g = False
                break
        if g==True:
            print("Prime")
        else:
            print("Not prime")
    elif k<=3 and k!=1:
        print("Prime")
    elif k==1:
        print("Not prime")
    li.append(k)
#print(li)
