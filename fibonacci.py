x = int(input("How many fibonacci numbers You need? ")) #user input how many numbers
lista = [] #list of numbers

def suma_2_ostatnich(): #sums two last numbers of list 'lista'
    return lista[-1] + lista[-2]

if x >= 1: #adds '1' to list if You need only 1 number
    lista.append(1)

if x >= 2: #adds 2x'1' to list if You need only 2 numbers
    lista.append(1)
    lista.append(1)

if x > 2: #adds the rest of fibonacci numbers
    for i in range(x-2):
        lista.append(suma_2_ostatnich())

print(lista)
