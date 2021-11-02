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
            
            

    def asking_for_answer(self):
        self.player1 = int(input("Player 1 answer: "))
        self.player2 = int(input("\nPlayer 2 answer: "))

        

    def korrekt_svar_tekst(self):
        p1=0
        p2=0
        final_answer = self.answers.title().split(",")
        print("\n\nCorrect answer: ",final_answer[int(self.correct_answer.title())],"\n\n")        
        if self.player1 ==  int(self.correct_answer.title()) :
            p1 = int(p1)+1
            print("Player 1: Correct")
        else: 
            print("Player 1: Wrong")
        if self.player2 ==  int(self.correct_answer.title()) :
            p2 = int(p1)+1
            print("Player 2: Correct")
        else:
            print("Player 2: Wrong")
            
        print("\nScore:","\nPlayer 1:",p1,"\nPlayer 2:",p2,"\n\n")
        

            #int(self.correct_answer.title()) 

                
                

