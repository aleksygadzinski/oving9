def read(file_name):
    from OPPGAVE_C import Question
    quest=list()
    a_file = open(file_name)
    line=a_file.readline()
    while line:
        splitted_line = line.split(":")
        splitted_line[2]=splitted_line[2].replace("[","")
        splitted_line[2]=splitted_line[2].replace("]","")
        quest.append(Question(splitted_line[0],splitted_line[1], splitted_line[2]))    
        line = a_file.readline()   
    return quest  
    #for a in quest:
        #print (a)

Questions = read("sporsmaalsfil.txt")
for Question in Questions:
    Question.asking()
    Question.asking_for_answer()
    Question.korrekt_svar_tekst()