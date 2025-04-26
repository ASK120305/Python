def series(lower,upper):
 print("Prime numbers between", lower, "and", upper, "are:")
 num=lower
 while(num<=upper):
    c=0 #checks the number of divisors
     # check for factors
    for i in range(1,num+1):
      if (num%i == 0):
        c=c+1
    if(c==2):
       print(num,"is a prime number")
    num=num+1
lower=int(input("Enter Lower limit of the series"))
upper=int(input("Enter Upper limit of the series"))
series(lower,upper)