import random
randomNumber = random.randrange(0,10)
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Your guess please: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done, your answer is perfect CONGRATULATIONS!")
    elif userInput>10:
        print("Our guess range is between 0 and 10, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 10, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

print("End of program")