def accept():
 lst=[]
 ans='y'
 while ans =='y' or ans=='Y':
  n=int(input('Enter a number: '))
  lst.append(n)
  ans=input('Enter more? y/n: ')
  print()
  tup=tuple(lst)
 return tup
def low_high():
 l=h=tup[0]
 for num in tup:
  if num<l:
    l=num
  elif num>h:
   h=num
 print ('Lowest number is: ', l)
 print ('Highest number is: ',h)
def sum_avg():
 sum = avg=0
 for num in tup:
  sum+=num
 l = len(tup)
 avg=sum/l
 print ('Sum: ',sum)
 print ('Average: ',avg)
while(1):
 print('''What do you want to do?
 1 To accept a set of numbers & create a Tuple
 2 To find the Lowest & highest Number from the Tuple 
 3 To find sum & average of all elements in the Tuple
 4 Exit''')
 ch = input ('Enter your choice : ')
 if ch=='1':
  tup=accept()
  print ('Tuple formed is: ',tup)
 elif ch=='2':
  low_high()
 elif ch=='3':
  sum_avg()
 elif ch=='4':
  exit()
else:
 print('Invalid choice entered')