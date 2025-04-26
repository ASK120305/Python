def factorial():
 n=int(input('enter a positive integer: '))
 if n==0:
  fact=0
 else:
  fact=1
 for i in range (1,n+1): fact*=i
 print ('Factorial of', n, 'is', fact)
def series():
 n=int(input('enter number till which you want to print fibonacci series: '))
 if n<0:
  print ('enter a positive number')
 else:
  a=0
  b=1
  c = a+b
  print (a,b, end = ' ')
  while c<=n:
   print (c, end = ' ')
   a=b
   b=c
   c=a+b
print()

while (1):
 print ('''what do you want to do?:
1 to find factorial of a number
2 to print fibonacci series up to entered term
3 exit''')
 ch=input('enter choice: ')
 print()

 if ch=='1':
  print ('Finding factorial...')
  factorial()

 elif ch=='2':
  print ('Fibonacci series...') 
  series()
 elif ch=='3':
   print("Bye bye!")
   exit()
   
 else:
  print('Invalid choice entered.')