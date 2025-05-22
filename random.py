import random as rd
user=input("Type the number: ")
if user.isdigit():
    user=int(user)

    if (user <=0):
        print("TYPE greater the number than 0")
        quit()

else:
    print("please type the number next time")
    quit()

randomx=rd.randint(0,user) 
guess=0

while True:
    guess+=1
    user2=input("type the guessed number: ")
    if user2.isdigit():
        user2=int(user2)
    else:
        print("please type the number next time..")
        continue

    if user2==randomx:
        print("you got it")
        break
    else:
        if user2 < randomx:
            print("you were above the number")
        else:
            print("you were below the number")
print("correct",str(guess),"gusse")







