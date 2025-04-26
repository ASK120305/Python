Queue= []
def push(Queue,val):
   Queue.append(val)
while True:
    choice=int(input("1-> Add\n 2->Enter your choice "))
    if choice == 1:
        val= int(input("Enter the number to push \n"))
        push(Queue,val)
        print(Queue)
    ch=input("Do you wanna add more number? Yes/No ")
    if ch in 'NoN':
      break
print("Goodbye!")




