inputs=[]
z=int(input())
for i in range(z):
    n= input()
    inputs.append(n)
even=""
odd=""
cok=[]
for word in inputs:
    j=0
    even=""
    odd =""
    for char in word:
        if j%2==0:
            even+=char
        else:
            odd+=char
        j+=1
    cok.append(even)
    cok.append(odd)
q=0

for i in range(z):
    print(cok[q],cok[q+1])
    q+=2
    
