x = int(input("Podaj jak długi ciąg licz fibonnaciego wyświetlić: "))
lista = []

def suma_2_ostatnich():
    return lista[-1] + lista[-2]

if x >= 1:
    lista.append(1)

if x >= 2:
    lista.append(1)
    lista.append(1)

if x > 2:
    for i in range(x-2):
        lista.append(suma_2_ostatnich())

print(lista)
    

input("\n\n\t\t\t \\ Aby zakończyć \n\t\t\tnaciśnij 'enter' \\")
