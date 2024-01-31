from tkinter import *
import hangman
import tictactoe
import rockpaperscisor
from tkinter import messagebox
gui = Tk()
gui.config(bg='black')
gui.geometry("900x350")
var=IntVar()
var.set(0)
def end():
    messagebox.showinfo("End","Thank you for playing")
    gui.destroy()
Heading=Label(text="Welcome to The Arcadia",font=("Helvetica 27 bold"),background='purple')

hButton = Button(text='Play Hangman',
width=40,height=3,command=hangman.hangman,background='green',font=("Helvetica", 15))

tButton = Button(text='Play Tic Tac Toe',
width=40,height=3,command=tictactoe.tictactoe,background='blue',font=("Helvetica", 15))

rButton = Button(text='Play Rock Paper and Scissor',
width=40,height=3,command=rockpaperscisor.rockpaperscisor,background='red',font=("Helvetica", 15))

eButton=Button(text="Stop Playing",command=end,width=30,height=2)

Heading.pack()
hButton.pack()
tButton.pack()
rButton.pack()
eButton.pack()

mainloop()