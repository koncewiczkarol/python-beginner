import random

print("\t Welcome in Cows and Bulls!!\n\n")

# create random 4 digit number and gets users guess number
number = str(random.randrange(1000, 9999))
guess = input(str("Enter Your 4-digit number: "))

# check if guess digits are cows or bulls
def add():
    for i in range(0, 4):
        if guess[i] == number[i]:
            result.append("cow")
        if guess[i] in number and guess[i] not in number[i]:
            result.append("bull")


while guess != number:
    result = [] 

# check if guess is 4 digit and only numbers
    while len(guess) != len(number) or guess.isdigit() == False:
        print("Wrong data format!")
        guess = input(str("Enter Your 4-digit number: "))
  
    add()

# if user match the number, break loop
    if guess == number:
        break

# if user did not match the number, tell how close it was
    if result:
        result.sort()
        result.reverse()
        print(result)
    else:
        print("You didn't match any number. Try againA")

# ask again for number        
    guess = input(str("Enter Your 4-digit number: "))

# if user guess the number    
print("You did it! It is", number)

input("\n\n\t\t\t \\ To quit \n\t\t\t press 'enter' \\")
