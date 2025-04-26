# first remove then add then reverse then replace
list = [2, 4, 5, 7, 9, 10]
list[0]="Zebra"
print(list)
list.reverse()
print(list)
i=-1
while i>-7:
    list2 = []
    list2.insert(0,list[i])
    print(list2)
    i=i-1
