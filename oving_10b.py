def spiller():
    from oving_10 import Spiller
    x = 0
    spiller_liste = list()
    antall_spillere = int(input("Skriv inn antall spillere: "))
    for spiller in range(int(antall_spillere)):
        spiller_navn = input("Skriv inn navn til Spiller", x)
        x=x+1
        spiller_liste.append(spiller_navn, 0)
    return spiller_liste    
    
