#sto importando il modulo random per generare numeri casuali
import random as r
#creo lista vuota di inumeri casuali
numeri_casuali = []
#la funzione fa si che vengano ripetuti 5 volte i numeri casuali con un range appunto da 0 a 50
for i in range(5):
    numeri_casuali.append(str(r.randint(0,50)))
#separiamo i numeri con degli spazi
separatore = " "
stringa_da_inserire = separatore.join(numeri_casuali)

#apre il file in modalità scrittura
with open("numeri.txt", "w") as file:
    file.write(stringa_da_inserire)


#apre file modalità lettura
with open("numeri.txt", "r") as file:
    stringa = file.read()
    print(stringa)


lista_da_indovinare = stringa.split(" ")
#print(lista_da_indovinare)

tentativi = 0
#ho tre tentativi per indovinare il numero
while tentativi < 3:
    num1 = input("Inserisci un numero intero tra 0 e 50: ")
    if num1 in lista_da_indovinare:
        print("numero indovinato")#se il numero è esatto uscirà numero indovinato
    else:
        print("numero non indovinato")#se il numero è errato avrai altre due possibilità di indovinare il numero
    
    tentativi+=1
#utilizzati tutti e tre i tentativi terminerà il programma e ci dirà che i tentativi sono terminati
print("Tentativi terminati")