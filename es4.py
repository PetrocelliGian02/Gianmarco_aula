#Gestione negozio

controllo = True

#Variabili 

selezione = input("ciao Gianmarco cominciamo...")

lista_prodotti = ["pallone", "gelato", "telecomando"]

#funzioni

if selezione == "si":
     
     while controllo:
          
          selezione2 = input("vuoi vedere pallone?")
          if selezione2.lower() == "si":
               print("operazione effettuata")
               

          selezione3 = input("vuoi vedere gelato? ")
          if selezione3.lower() == "si":
               print("operazione effettuata")
                 
          
          selezione4 = input("vuoi vedere telecomando?")
          if selezione4.lower() == "si":
               print("operazione effettuata")
               

          selezioneFinale = input("vuoi uscire?")
          if selezioneFinale.lower() == "si":
               print("operazione effettuata")
               break
          
          
