import random

print('number guessing game ')



number = random.randint(1, 9)

chances = 0
while chances <5:
 
    guess=int(input("enter a number between 1-9"))

    if guess == number:

        print("you won!!!")

        break

    elif guess < number:
        print ("your guess is too low")

    else:
        print("your guess is too high")

    chances += 1

if not chances <5:
    print("you lose, the number is",number)
