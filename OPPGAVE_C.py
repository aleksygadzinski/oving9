class Question:
    def __init__(self, question, correct_answer, answers):  
        self.question = question
        self.correct_answer = correct_answer  
        self.answers = answers

        
    def asking(self):
        print("Question:\n",self.question.title(), "\n")
        final_answer = self.answers.title().split(",")
        for x in final_answer:
            index = final_answer.index(x)
            print(index,": ",x,"\n")
            
            

    def asking_for_answer(self, s_l):
        for player in s_l: 
            
            print(player.navn,"answer")
            svar = int(input(": "))
            
            if svar ==  int(self.correct_answer.title()) :
                
                #print(item,": Correct")
               
                player.add_points()
                
           #else: 
                #print(item,": Wrong! What a noob")