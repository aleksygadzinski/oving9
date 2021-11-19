
class Spiller:
    def __init__(self, navn, poengsum):
        self.poengsum = 0
        self.navn = navn

    def something():
        #import pandas as pd
        spiller_liste = list()
        #spil2 = list()
        s_antall = int(input("Skriv inn antall spillere: "))
        
        points = [0]*s_antall
        for spiller in range(int(s_antall)):
            spiller_navn = input("Skriv inn navn til Spiller: ")
            spiller_liste.append(spiller_navn)
       # self.navn.title() = spiller_navn
        self.navn = spiller_liste
        #self.poengsunm.title() = 0
        self.poengsum = 0   
        
        
        
Spiller.something()          
s = Spiller()        
s.something()            
            
'''
            
            spiller_liste.append(spiller_navn)
            
            
            
        
        spiller_liste = spil2
        d = {'Spiller:': spiller_liste , 'Poengsum:':points}
        df = pd.DataFrame(data=d)
        print(df)
        return s_antall
        return spiller_liste
        return spil2
 
'''                
    
'''        
    def spiller(self):
    
        x = 0
        spiller_liste = list()
        antall_spillere = int(input("Skriv inn antall spillere: "))
        for spiller in range(int(antall_spillere)):
            spiller_navn = input("Skriv inn navn til Spiller", x)
            x=x+1
            spiller_liste.append(spiller_navn, 0)
        return spiller_liste  
'''