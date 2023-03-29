import tkinter as tk
import random as rndm

#window settings
root = tk.Tk()
root.geometry('400x600')
root.title('flashcards')

#takes  the answers and questions from .txt file

with open('Questions.txt', 'r') as  Q:
    QuestionsList = Q.read().splitlines()
with open('RightAnswers.txt', 'r') as  A:
    AnswersList = A.read().splitlines()


#compares Question and Answer location on the list
Question = rndm.choice(QuestionsList)
AnswerIndex = QuestionsList.index(Question)
RightAnswer = AnswersList[AnswerIndex]


#checks is the answer the same as Right Answer
def Check():
    #global make var accesible for all of the code
    global RightAnswer
    Answer = Entry.get()
    if RightAnswer == Answer:
        IsItCorrect.config(text= 'Correct', fg = '#00FF00')
        IsItCorrect2.config(text='')
        
            
        #clears  Entry Pool;Note for myself: 0, tk.END means that it will only clear from the first to the last character, not all pool
        Entry.delete(0, tk.END)
        #new question for making it loop
        NewQuestion = rndm.choice(QuestionsList)
        QuestionLabel.config(text=NewQuestion)
        #new answer
        NewAnswerIndex = QuestionsList.index(NewQuestion)
        RightAnswer = AnswersList[NewAnswerIndex]
    else:
        IsItCorrect.config(text='Nope, the answer is:', fg = '#FF0000')
        IsItCorrect2.config(text=RightAnswer, fg = '#FF0000')
    IsItCorrect.pack()
    IsItCorrect2.pack()
    

#header
Header = tk.Label(root, text='Flashcards', font=('Comic Sans MS', 35))
Header.pack()

#Question
QuestionLabel = tk.Label(root, text=Question, font=('Arial', 20))
QuestionLabel.pack()

#Answer
Entry = tk.Entry(root, width= 30)
Entry.pack()

#submit button
Submit = tk.Button(root, text='Submit', command=Check,)
Submit.pack()

#shows that answer was correct or not
IsItCorrect = tk.Label(root, text='',  font=('Arial', 15))
#label for the right answer
IsItCorrect2 = tk.Label(root, text='', font=('Arial', 15))

root.mainloop()