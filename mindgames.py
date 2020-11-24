from tkinter import *
from tkinter import messagebox
import os

def tictactoe():
	os.system('python tictactoe.py')
def fliptiles():
	os.system('python fliptiles.py')
def twozerofoureight():
	os.system('python main.py')

root = Tk()
root.geometry('480x350')
root.configure(bg="skyblue")
root.title("Mind Games")

reglbl = Label(root, text="Mind Games",width=20,font=("bold",20))
reglbl.place(x=80,y=20)

b1=Button(root, text='Tic Tac Toe',width=10,bg='Green',fg='white',command=lambda:tictactoe())
b1.place(x=190,y=80)
b2=Button(root, text='Flip Tiles',width=10,bg='Green',fg='white',command=lambda:fliptiles())
b2.place(x=190,y=120)

b3=Button(root, text='Exit',width=10,bg='Red',fg='white',command=root.destroy)
b3.place(x=190,y=160)

root.mainloop()