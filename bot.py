from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
engine=pp.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)




def speak(word):
    engine.say(word)
    engine.runAndWait()




chatbot=ChatBot('my bot')
trainer=ListTrainer(chatbot)
trainer.train(['hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Neha',
   'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in ur pc',
    'In which language you talk?',
    ' I mostly talk in english','what do u like most',
    'I always there for ur work',
    'tell me about urself bot',
    'okay I m bot created by Neha I m here for  ur help how can i help you thank you',
    'thank you',
    'welcome',
    'bye',
    'bye nice to meet  you'])

#print("Talk to bot")
#while True:
   # request=input('you: ')
    #response=chatbot.get_response(request)
    #print('Bot:', response)'''
    
main=Tk()



main.geometry("500x650")
main.title("MY CHAT BOT")
img=PhotoImage(file="robo.png")
photoL=Label(main, image=img)
photoL.pack(pady=5)






def ask_from_bot():
    query = textF.get()
    answer = chatbot.get_response(query)
    msg.insert(END,"you:"+query)
    msg.insert(END, "bot : " + str(answer))
    speak(answer)
    textF.delete(0, END)
    msg.yview(END)
    print("clicked")

frame=Frame(main)
sc=Scrollbar(frame)
msg=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

textF=Entry(main,font={"verdana",20})
textF.pack(fill=X,pady=10)
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()
main.bind('<Return>',enter_function)
main.mainloop()