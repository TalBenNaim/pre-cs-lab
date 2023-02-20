import random
num = random.randint(1,100)

userNum = int(input("Guess a number? \n"))

if userNum == num:
    print("Good guess!")
elif userNum > num:
    print("You need to guess smaller number.")
else:
    print("you need to guess bigger number.")