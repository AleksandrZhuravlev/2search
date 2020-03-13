import random
list=[]
listlen=int(input())
searched=input()
for i in range(listlen):
    list.append(random.randint(1,10))
print(list)

inf=0
sup=listlen
average=len(list) // 2
list.sort()

for i in range(listlen):
