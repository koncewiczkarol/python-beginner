dlugosc = int(input("Wprowadź długość hasła (ilość znaków) do wygenerowania: "))

litery = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
znaki = ["!", "@", "#", "$", "%"]

haslo_final = str("")

import random

for i in range(dlugosc):
    x = random.randrange(0,6)
    if x < 2:
        y = random.choice(litery)
        haslo_final += y
    elif x == 2:
        y = random.choice(litery)
        haslo_final += y.upper()
    elif x == 3 or x == 4:
        y = random.choice(cyfry)
        haslo_final += y
    elif x == 5:
        y = random.choice(znaki)
        haslo_final += y

print(haslo_final)


input("\n\n\t\t\t \\ Aby zakończyć \n\t\t\tnaciśnij 'enter' \\")
