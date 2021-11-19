class Spiller:
    def __init__(self, navn, poengsum):  
        self.navn = navn
        self.poengsum = poengsum
        
    def get_points(self):
        return self.poengsum
    
        
    def add_points(self):
        self.poengsum +=1
        
        
'''        
        
s_l= list()
n_p = int(input("write the number of players: "))
i=0
points = [0]*n_p
for player in range(n_p):
    i=i+1
    print("\n\nPlayer",i, "name")
    p_n = input(": ")
    s_l.append(p_n)
    players = Spiller(s_l,points)   
players.show_points()
          

            
            

#players = Question(s_l,points)   
#players.show_points()
#game = Question.something()3
'''