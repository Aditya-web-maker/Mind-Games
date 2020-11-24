import tkinter as tk
import random
import sqlite3

sqliteConnection = sqlite3.connect('psrgames.db')
cursor = sqliteConnection.cursor()
create_database_query = "CREATE TABLE IF NOT EXISTS fliptiles (id INTEGER NOT NULL UNIQUE, score VARCHAR(50) NOT NULL,PRIMARY KEY(id AUTOINCREMENT));"
cursor.execute(create_database_query)

pressed = -1
flipped_tiles = 16
moves = 0
high_score = 0

def check_win():
    global high_score, moves
    
    if flipped_tiles == 0:
        
        if moves <= high_score or high_score == -1:
            high_score = moves
            f = open('high_score.txt', 'w')
            f.write(str(high_score))
            f.close()
        insert_val = str(moves)
        count = cursor.execute("INSERT INTO fliptiles (score)  VALUES  (?)", (insert_val,))
        sqliteConnection.commit()  
        
        win_lbl['text']='CLICKS: '+str(moves)+', BEST: '+str(high_score)
        sqliteConnection.close()       
        
def print_moves():
    win_lbl['text'] = 'CLICKS: ' + str(moves)


def new_game():
    global pressed, flipped_tiles, buttons, colours, moves, win_lbl, high_score
    pressed = -1
    flipped_tiles = 16
    moves = 0
    buttons = {}
    win_lbl['text'] = ''

    f = open('high_score.txt', 'r')
    high_score = int(f.readline().strip())
    f.close()

    random.shuffle(colours)

    ind=0
    for i in range(4):
        for j in range(4):
            btn = buttonclass(ind)
            buttons[ind] = btn
            if ind!= len(colours)-1: 
                ind+=1
        
    ind=0
    for i in range(4):
        for j in range(4):
            buttons[ind].bttn.grid(row=i, column=j, sticky='nsew')
            if ind!= len(colours)-1: 
                ind+=1


class buttonclass:
    
    def __init__(self, ind):
        self.index = ind
        self.bttn = tk.Button(frm,
                             width=8, height=4,
                             bg='skyblue', activebackground = colours[self.index],
                             command=self.btn_press
                             )
    def btn_press(btn):
        global pressed, moves
        btn.bttn.configure(bg=colours[btn.index])
        moves += 1
        print_moves()
        if pressed == -1:
            pressed = btn.index
        else:
            btn.compare_pressed_btns()
    
    def compare_pressed_btns(btn):
        global pressed
        global flipped_tiles

        if (colours[btn.index] != colours[pressed]):
            btn.bttn.configure(bg='skyblue')
            buttons[pressed].bttn.configure(bg='skyblue')
            pressed = -1

        elif colours[btn.index] == colours[pressed] and (btn.index != pressed):
            btn.bttn['state'] = tk.DISABLED
            buttons[pressed].bttn['state']= tk.DISABLED
            pressed = -1
            flipped_tiles -= 2
            check_win()

        elif  btn.index == pressed:
            btn.bttn.configure(bg='skyblue')
            pressed = -1
       

root = tk.Tk()
root.title('Flip Tiles')
root.config(bg = 'black')

frm = tk.Frame(root, bg='Gray')
frm.grid(row = 1, column=0, sticky='nsew')

frm.rowconfigure(list(range(4)), minsize=50)
frm.columnconfigure(list(range(4)), minsize=50)

buttons = {}
colours=2*['yellow', 'Violet', 'red', 'gray', 'white', 'Orange','#c34', 'ForestGreen']
random.shuffle(colours)

frm2 = tk.Frame(root, bg='black')

win_lbl = tk.Label(frm2,
                  width=19, height=1,
                 bg='white',
                 relief=tk.GROOVE,
                 borderwidth=2)
win_lbl.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')


new_game_btn = tk.Button(text='NEW GAME',
                        master=frm2,
                       width=13, height=1,
                       bg='#19eeae',
                       command=new_game)
new_game_btn.grid(row=0, column=1, padx=5, pady=5, sticky = 'nsew')

frm2.grid(row=0, column=0, sticky='nsew')

new_game()

root.mainloop()
