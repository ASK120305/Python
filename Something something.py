def cnt():
    f=open("D:\\Python2.0\\Book.txt", "r")
    cont=f.read()
    print(cnt)
    v=0
    cons=0
    lcl=0
    ucl=0
    for ch in cont:
        if (ch.islower()):
            lcl+=1
        elif (ch.isupper()):
            ucl+=1
        ch=ch.lower()
        if(ch in['a','e','i','o','u']):
            v+=1
        elif (ch in['b','c','d','f','g',
 'h','j','k','l','m',
 'n','p','q','r','s',
 't','v','w','x','y','z']):
               cons+=1
    f.close()
    print("Vowels are:" ,v)
    print("Consanants are:", cons)
    print("Lowerclass letters are:", lcl)
    print("Upper case letters are:", ucl) 