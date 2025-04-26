def add(a,val):
 a.append(val)
 print("Entering the number successfully")

def Display(a):
 print(a)

def pop(a):
 val= a.pop()
 print("Deleted value successfully")
a = []
while True:
    choice=int(input("1-> Add\n 2-> Pop\n 3->Display\n 4->Peek\n 5->Exit\n 6->Enter your choice "))
    if choice == 1:
        val= int(input("Enter the number to push \n"))
        add(a,val)
        print(a)
       
    elif choice==2:
        val=int(input("Enter the number to pop \n"))
        pop(a)
        print(a)
      
    elif choice==3:
        val=str(input("Display the list? \n"))
        if val==("yes"):          
            Display(a)
            print("List has been displayed")
        else:
            print("Access Denied!")
            
       


