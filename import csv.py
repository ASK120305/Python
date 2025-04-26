import csv
while(1):
 print()
 print ('''what do you want to do?
 1 enter records
 2 print records
 3 search record using employee number
 4 display record of employee having highest salary
 5 exit''')
 ch = input('enter your choice: ')
 if ch=='1':
  f=open(r'employee.csv','a')
  cw = csv.writer(f)
  empno = input('enter employee code: ')
  name = input('enter employee name: ')
  sal = int(input('enter employee salary: '))
  lst = [empno, name, sal]
  cw.writerow(lst)
  f.close() 
 elif ch=='2':
  f=open(r'employee.csv','r', newline='\n')
  print('EMP NO \t\t NAME \t\t SALARY')
  cr=csv.reader(f)
  for rec in cr:
   print(rec[0], '\t', rec[1], '\t', rec[2])
  f.close()
 elif ch=='3':
  f=open(r'employee.csv','r', newline='\n')
  en = input('enter empoyee number to search for: ')
  cr=csv.reader(f)
  for rec in cr:
   if rec[0]==en:
    print('EMP NO \t NAME \t SALARY')
    print(rec[0], '\t', rec[1], '\t', rec[2])
    break
   else:
     print ('record not found')
  f.close()
 elif ch=='4':
  lst=[]
  data=[]
  f=open(r'employee.csv','r', newline='\n')
  cr=csv.reader(f)
  for rec in cr:
   data.append(rec)
   lst.append(rec[2])
   smax=max(lst)
   i=lst.index(smax)
  print (data[i])
  f.close()
 elif ch=='5':
  exit()
else:
 print('invalid choice entered')