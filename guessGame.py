import random

lower = int(input("Enter lower value: "))
upper = int(input("Enter upper value: "))

randomGameValue = random.randint(lower, upper)

attemptController = 0
attemptList = []


while True:
    print("Guess the value in the range of", lower, "to", upper,": ")
    yourValue = int(input())
    attemptList.append(yourValue)
    attemptController = 1

    if attemptController == 1:
       print("\nYour attempts: ", attemptList, "\n") 

    if yourValue == randomGameValue:
        print("Congratulations,", yourValue, "is the number")
        break
    elif yourValue > randomGameValue:
        print("Your value is too high, please try again!\n\n")
    else: 
        print("Your value is too low, please try again!\n\n")



print("\nFinshed Algorithm")