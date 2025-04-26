def teri():
    c=0
    f=open("India.txt", "r")
    for l in f:
        w=l.split()
        for W in w:
            if W=="India":
                c+=1
        print(c)
    f.close()