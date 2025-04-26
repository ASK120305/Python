def cnt():
 f=open("D:\\Python2.0\\Book.txt","r")
 cont=f.read()
 print(cnt)
 v=0
 cons=0
 l_c_l=0
 u_c_l=0
 for ch in cont:
  if (ch.islower()):
   l_c_l+=1
  elif(ch.isupper()):
   u_c_l+=1
 ch=ch.lower()
 if( ch in ['a','e','i','o','u']):
  v+=1
 elif (ch in ['b','c','d','f','g',
 'h','j','k','l','m',
 'n','p','q','r','s',
 't','v','w','x','y','z']):
  cons+=1
 f.close()
print("Vowels are : ",v)
print("consonants are : ",cons)
print("Lower case letters are : ",l_c_l)
print("Upper case letters are : ",u_c_l)
#main program