ylist= []
print("Enter 5 elements for the list: ")
for i in range(5):
    val = int(input())
    mylist.append(val)

print("Enter an element to be search: ")
elem = int(input())

for i in range(5):
    if elem == mylist[i]:
        print("\nelement found at index:" , i)
        print("Element found at position:" , i+1)
