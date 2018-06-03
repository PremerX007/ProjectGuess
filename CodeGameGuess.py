import random

number = random.randint(1, 30)
tries = 1
win = False

name = input("Hi...what you name??")

print("Wow!!", name + " , This name so cool.")

question = input("play my game [Y/N]")
if question.lower() == "n":
        print("Okay...TT")
        print("Press Enter To Continue........")
        input()
        input(quit())

if question.lower() == "y":
        print("Let's Go")
        print("I will let you guess number from 1 to 30")    
while not win:
    guess = int(input("Number : "))
    tries = tries + 1
    if guess == number:
        win = True
    elif guess < number:
        {
            print("lowNumber")
        }
    elif guess > number:
        {
            print("HigherNumber")
        }

print("correct. the number is {}".format(number))
print("trise {} Hahaha" .format(tries))
input("Press Enter To Continue........")
