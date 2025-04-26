#practical number 8+10
file =open("D:\Python 2.0\Book.txt", "r")
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+'#',end="")
    print("")
file.close()
fo=open("Book2.txt", "x")
fn=open("Book3.txt", "x")
for i in lines:
    if 'a' in i:
        fn.write(i)
    else:
        fo.write(i)
fn.close()
fo.close()
print("Lines containing character a has been removed")
print("Lines containing character a has been saved in a different book")
