import random

meh = random.randint(1,9)
print("Number Guessing Game")
bleh = 0
print("Guess the number between 1 and 9 or die :)")
while bleh<5:
    eh = int(input("Enter your guess : "))
    if eh == meh:
        print("Congratulations~!")
        break
    elif eh<meh:
        print("Guess a higher number.")
    else :
        print("Guess a lower number.")    
    bleh +=1
if not bleh<5:
    print("Congratulations you lost~!!")
    print("The number was " , meh)