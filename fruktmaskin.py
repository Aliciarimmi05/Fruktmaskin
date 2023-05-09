#visar vad funktioner är, vad de har för nytta dvs slippa repetera kod
import random

#skapar en tuple, finns set och arrays också
frukter = ("Carambola", "pitaya", "rambutan", "guava")
looping = True

#Definerar en python funktion
def print_fruit(userinput) :
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här!\n")



while looping:
    print("--------------------------------------")
    print("\n-:FruktAutomat:-\n")

    i = 1
    for frukt in frukter:
        print(str(i) + ": "+ frukt)
        i += 1

    fruktnr = input("\nMata in sifftra för vald frukt: ")
    #intitierar funktioner 1 gång

    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till j/n ")
    print("\n")
    if (go == "n"):
        break

    print("-------------------------------------")
    print("Förresten, du får en frukt till!")
    slumpfruktnr = random.randint(1, 5)
    print_fruit(slumpfruktnr)