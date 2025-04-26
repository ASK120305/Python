book=[]
def push():
    bcode=input("Enter code ")
    btitle=input("Enter book title ")
    price=input("Enter price ")
    bk=(bcode,btitle,price)
    book.append(bk)
def pop():
    if book==[]:
        print("Underflowing stack is empty")
    else:
        bcode,btitle,price=book.pop()
        print("Popped element is ")
        print("bcode",bcode,"btitle",btitle,"price",price)
def traverse():
    if not book==[]:
        n=len(book)
        for i in range(n-1,-1,-1):
            print(book[i])
    else:
        print("Book is empty")
while True:
 print("1.Push")
 print("2.Pop")
 print("3.Traversal")
 print("4.Exit")
 ch=int(input("Enter your choice "))
 if ch==1:
    push()
 elif ch==2:
    pop()
 elif ch==3:
    traverse()
 elif ch==4:
    print("End")
    break
 else:
    print("Invalid choice")
