import tkinter as tk
from tkinter import StringVar
root=tk.Tk()
root.geometry("700x700")
questions=["1+1=?","2+2=?","3+3=?","4+4=?","5+5=?"]
options=[["3","4","2","6","1"],["2","4","6","8","5"],["1","4","5","6","6"],["8","4","5","6","8"],["6","10","7","8","10"]]
frame=tk.Frame(padx=10,pady=10,bg='#fff')
question_label=tk.Label(frame,height=5,width=28,bg='#ddd',font=('Verdana',20),wraplength=500)
v1=StringVar(frame)
v2=StringVar(frame)
v3=StringVar(frame)
v4=StringVar(frame)
v5=StringVar(frame)

option1=tk.Radiobutton(frame,bg='#fff',variable=v1,font=('Verdana',20),command=lambda:checkAnswer(option2))
option2=tk.Radiobutton(frame,bg='#fff',variable=v2,font=('Verdana',20),command=lambda:checkAnswer(option1))
option3=tk.Radiobutton(frame,bg='#fff',variable=v3,font=('Verdana',20),command=lambda:checkAnswer(option3))
option4=tk.Radiobutton(frame,bg='#fff',variable=v4,font=('Verdana',20),command=lambda:checkAnswer(option1))
option5=tk.Radiobutton(frame,bg='#fff',variable=v5,font=('Verdana',20),command=lambda:checkAnswer(option1))
button_next=tk.Button(frame,text='Next',bg='orange',font=('Verdana',20),command=lambda: displayNextQuestion())
frame.pack(fill='both',expand=True)
question_label.grid(row=0,column=0)
option1.grid(sticky='W',row=1,column=0)
option2.grid(sticky='W',row=2,column=0)
option3.grid(sticky='W',row=3,column=0)
option4.grid(sticky='W',row=4,column=0)
button_next.grid(row=6,column=0)
index=0
correct=0
def disableButtons(state):
    option1['state']=state
    option2['state']=state
    option3['state']=state
    option4['state']=state
def checkAnswer(radio):
    global correct,index

    if radio['text']==options[index][4]:
        correct+=1

    index+=1
    disableButtons('disable')

def displayNextQuestion():
    global index,correct
    if button_next['text']=='restart the quiz':
        corret=0
        index=0
        question_label['bg']='grey'
        button_next['text']='next'
    if index==len(options):
        question_label['text']=str(correct)+"/"+str(len(options))
        button_next['text']='restart the quiz'
        if correct>=len(options)/2:
            question_label['bg']='green'
        else:
            question_label['bg']='red'
            
    else:
        question_label['text']=questions[index]
    disableButtons('normal')
    opts=options[index]
    option1['text']=opts[0]
    option2['text']=opts[1]
    option3['text']=opts[2]
    option4['text']=opts[3]
    v1.set(opts[0])
    v2.set(opts[1])
    v3.set(opts[2])
    v4.set(opts[3])
    if index==len(options)-1:
        button_next['text']='check the results'

displayNextQuestion()
root.mainloop()

        
    
