def checkleapyear(year):
    if (year%400==0) and (year%100!=0):
          print("This shit", year, "leap year")
    elif (year%4==0) and (year%100!=0):
         print("this shit", year, "Leap year")
    else:
         print("This shit not leap year")

year=int(input("enter year retard: "))
checkleapyear(year)