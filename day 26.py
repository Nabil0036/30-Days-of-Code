# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input().split()
b = input().split()

day = int(a[0])-int(b[0])
mon = int(a[1])-int(b[1])
year = int(a[2])-int(b[2])
#print(day,mon,year)
total_day = day + mon*30 + year*365
if total_day>0:
    if year>0:
        fine =10000
    else:
        if mon>0:
            fine = mon*500
        else:
            if day>0:
                fine = day *15
            else:
                fine =0
            
else:
    fine = 0
print(fine)
#print(total_day)
