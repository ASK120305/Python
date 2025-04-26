import pickle
def write():
 f=open("Studentdetails.dat","wb")
 while True:
  r=int(input("Enter the roll no.="))
  n=input("Enter the name=")
  Data=[r,n]
  pickle.dump(Data,f)
  ch=input("Do you want to add more (Y/N)=")
  if ch in 'nN' :
     break
 f.close()
def read():
 f=open("Studentdetails.dat","rb")
 try:
   while True:
    rec=pickle.load(f)
    print(rec)
 except EOFError:
  f.close()
def searchroll():
 found=0
 rollno = int(input("Enter the rollno to search =" ))
 f= open("Studentdetails.dat","rb")
 try:
  while True:
   rec=pickle.load(f)
   if rec[0]==rollno:
    print(rec[1])
    found=1
    break
 except EOFError:
  f.close()
 if found==0:
   print("Sorry record not found")
write()
read()
searchroll()