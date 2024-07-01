class Libro:
    def _init_(self, titolo, autore, pagine ):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    def __str__(self):
        return f"il libro:{self.titolo}, è stato scritto da: {self.autore}, ed ha: {self.pagine}"
         
libro1= Libro ("Divina commedia" "Alighieri" "370")

print(libro1.descrizione())


       