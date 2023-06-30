from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " сейчас ходит"))

            elif check_winner() is True:
                label.config(text=(players[0]+ " победил"))

            elif check_winner() == "Ничья":
                label.config(text=("Ничья!"))
        else:
                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0] + " сейчас ходит"))

                elif check_winner() is True:
                    label.config(text=(players[1] + " победил"))

                elif check_winner() == "Ничья":
                    label.config(text=("Ничья!"))



def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='#70fa95')
            buttons[row][1].config(bg='#70fa95')
            buttons[row][2].config(bg='#70fa95')
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[column][0].config(bg='#70fa95')
            buttons[column][1].config(bg='#70fa95')
            buttons[column][2].config(bg='#70fa95')
            return True


    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='#70fa95')
        buttons[1][1].config(bg='#70fa95')
        buttons[2][2].config(bg='#70fa95')
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='#70fa95')
        buttons[1][1].config(bg='#70fa95')
        buttons[2][0].config(bg='#70fa95')
        return True

    elif empty_spaces() is False:
        buttons[0][0].config(bg='#f3ff6b')
        buttons[0][1].config(bg='#f3ff6b')
        buttons[0][2].config(bg='#f3ff6b')
        buttons[1][0].config(bg='#f3ff6b')
        buttons[1][1].config(bg='#f3ff6b')
        buttons[1][2].config(bg='#f3ff6b')
        buttons[2][0].config(bg='#f3ff6b')
        buttons[2][1].config(bg='#f3ff6b')
        buttons[2][2].config(bg='#f3ff6b')
        return "Ничья"

    else:
        return False
def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player

    player = players[0]

    label.config(text=player+" сейчас ходит")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='')

window = Tk()
window.title("Крестики нолики")
players = ['x', 'o']
player = random.choice(players)
player = players[0]
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


label = Label(text= player + ' сейчас ходит', font=('Roboto', 40))
label.pack(side="top")

reset_button = Button(text="начать заново", font=("Roboto", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=("Roboto", 40), width=5, height=2,command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()