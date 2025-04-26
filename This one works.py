files= open("D:\\Python 2.0\\Book.txt", "r")
# read text file line by line
lines=files.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+"#", end="")
print("")