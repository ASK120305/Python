file = open("D:\\Python2.0\Book.txt","r")
# read text file line by line
lines = file.readlines()
for line in lines:
 words = line.split()
 for word in words:
  print (word+"#", end = "")
 print(" ")
