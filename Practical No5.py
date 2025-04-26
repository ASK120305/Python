def accept():
 st= input('enter string: ')
 return st
def print_st():
 global s
 print(s)
def count():
 global s
 lst = s.split()
 print (' No. of words in the string are: ', len(lst))
def longest():
 global s
 lst= s.split()
 longest=lst[0]
 for word in lst:
  if len(word)>len(longest):
   longest=word
 pos = lst.index(longest)
 print ('The longest word in the string is:', longest)
 print( 'And its position is: ', pos)
while(1):
 print()
 print ('''What do you want to do?
 1. To accept a string
 2. To print the string
 3. To count the total no. of words in the given string.
 4. To find the longest word & print its position.
 5. Exit''')
 ch = input('enter your choice: ')
 if ch == '1':
  s = accept()
 elif ch == '2':
  print_st()
 elif ch=='3':
  count()
 elif ch=='4':
  longest()
 elif ch== '5':
  exit()
 else:
  print('Invalid choice entered')