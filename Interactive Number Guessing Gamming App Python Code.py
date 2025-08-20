import random  #This allows the program to generate a random number
pythonr_number = random.randint(1, 10)    #This line picks a random number between 1 and 10, and stores it in the variable pythonr_number.The user must try to guess this number.


chance = 0
while chance < 3:  #  Destination chance value
    Customer_number = input("Guess a number from 1 to 10: ")
    chance += 1  # 3 Increment chance
    if Customer_number.isdigit() and int(Customer_number) == pythonr_number:   #Check match
        print("Correct guess!")
        break  # Exit loop
    else:  # If guess is wrong
        print("Wrong guess... try again")
        print("Chances left:", 3 - chance)  # <-- Added line to show remaining chances

else:  # Executed if loop completes without break
    print("Chance over... the correct number was", pythonr_number)
