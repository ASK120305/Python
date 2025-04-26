import random
while True:
    print("="*50)
    print("Rolling Dice, you ready? Lesgooo!!")
    print("*"*50)
    num=random.randint(1,6)
    if num==6:
        print("Yay! You got=", num , "You are legen......wait for it.......dary! Legendary!")
    elif num==5:
        print("Oooh you were close.....You got=", num)
    else:
        print("Nice try....You got=", num)
    ah=input("Do you still wanna try your luck? y/n= ")
    if ah in 'nN':
        break
print("So soon? well see you later, thanks for playing!")