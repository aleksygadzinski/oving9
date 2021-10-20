
class Question:
    def __init__(self, question, answer1, answer2, answer3, correct_answer):  
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct_answer = correct_answer  
        
    def asking(self):
         
        print(q1.question)
        print(q1.answer1)
        print(q1.answer2)
        print(q1.answer3)
     
    def asking_for_answer(self):
        answer = int(input("Write the number of the anwser: "))
        check = int(input("Good work! To check the answer type '1': "))
        
      
        if check == 1:
            if answer == int(q1.correct_answer) :
                print("Correct anwser!")
            else:
                print("Wrong anwser.")
        
q1 = Question("Question: What's 9 plus 10\n","1. It's 21","2. It's 19", "3. It's 69","2")

q1.asking()
q1.asking_for_answer()




