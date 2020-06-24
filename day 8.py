import sys

phone_book = {}
inputlist=[]
for line in sys.stdin:
    inputlist.append(line)

n = int(inputlist[0])
entries = inputlist[1:n+1]
queries = inputlist[n+1:]

for entry in entries:
    name,phone = entry.split()
    phone_book[name]=phone

for q in queries:
    que = q.rstrip()
    if que in phone_book:
        phone = phone_book[que]
        print(que + "=" + str(phone))
    else:
        print("Not found")
