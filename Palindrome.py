def palindrome():
    length=len(string)
    mid=int(length/2)
    rev=-1

    for a in range(mid):
        if string[a]==string[rev]:
            a=a+1
            rev=rev-1
        else:
            print(string,"is not a palindrome")
            break
    else:
        print(string,"is palindrome")

string=input("Enter any string=")
palindrome()


