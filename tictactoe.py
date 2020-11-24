from tkinter import *
import tkinter.messagebox
import sqlite3

sqliteConnection = sqlite3.connect('psrgames.db')
cursor = sqliteConnection.cursor()
create_database_query = "CREATE TABLE IF NOT EXISTS tictactoe (id INTEGER NOT NULL UNIQUE, player_a VARCHAR(50) NOT NULL, player_b VARCHAR(50) NOT NULL, result	VARCHAR(50) NOT NULL,PRIMARY KEY(id AUTOINCREMENT));"
cursor.execute(create_database_query)

root = Tk()
root.title("Tic Tac Toe")

playera = StringVar()
playerb = StringVar()
playerawins = StringVar()
playerbwins = StringVar()
p1_entry = StringVar()
p2_entry = StringVar()

player1_name = Entry(root, textvariable=p1_entry)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(root, textvariable=p2_entry)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, playera, playerbwins, playerawins

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerbwins = p2_entry.get() + " Wins!"
        playerawins = p1_entry.get() + " Wins!"
        playerb = p2_entry.get() 
        playera = p1_entry.get() 
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerawins)
        insert_query = """INSERT INTO tictactoe (player_a, player_b, result)  VALUES  (?,?,?)"""
        insert_val = (playera, playerb, playerawins)
        count = cursor.execute(insert_query, insert_val)
        sqliteConnection.commit()
        cursor.close()

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Draw")
        insert_query = """INSERT INTO tictactoe (player_a, player_b, result)  VALUES  (?,?,?)"""
        insert_val = (playera, playerb, "Draw")
        count = cursor.execute(insert_query, insert_val)
        sqliteConnection.commit()
        cursor.close()


    elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerbwins)
        insert_query = """INSERT INTO tictactoe (player_a, player_b, result)  VALUES  (?,?,?)"""
        insert_val = (playera, playerb, playerbwins)
        count = cursor.execute(insert_query, insert_val)
        sqliteConnection.commit()
        cursor.close()

buttons = StringVar()

label = Label(root, text="Player A:", font='Times 16 bold', bg='plum', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label(root, text="Player B:", font='Times 16 bold', bg='plum', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(root, text=" ", font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(root, text=' ', font='Times 16 bold', bg='#19eeae', fg='black', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

root.mainloop()
