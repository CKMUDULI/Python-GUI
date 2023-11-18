from tkinter import *

appwin = Tk()
appwin.title("Tic-Tac-Toe")

turn = "X"
main_label = Label(master=appwin, font=("ink free", 20, "bold"), text=f"{turn}'s turn")
main_label.pack()

records={key:"" for key in range(1,10)}
# records = dict()

def reset_all():
    global turn
    global records
    for widget in buttons_frame.winfo_children():
        widget.configure(cnf={"text":"", "font":("ink free", 20,"bold"), "height":"1", "width":"4", "relief":"groove","state":"normal"})
        turn="X"
        records={key:"" for key in range(1,10)}
        set_label()

def check_wnr():
    if "" not in records.values():
        main_label.config(text="Game Draw!")
        return True
    elif (records[1]==records[2]==records[3]=="X") or (records[4]==records[5]==records[6]=="X") or (records[7]==records[8]==records[9]=="X") or (records[1]==records[4]==records[7]=="X") or (records[2]==records[5]==records[8]=="X") or (records[3]==records[6]==records[9]=="X") or (records[1]==records[5]==records[9]=="X") or (records[3]==records[5]==records[7]=="X"):
        main_label.config(text="X wins")
        return True
    elif (records[1]==records[2]==records[3]=="O") or (records[4]==records[5]==records[6]=="O") or (records[7]==records[8]==records[9]=="O") or (records[1]==records[4]==records[7]=="O") or (records[2]==records[5]==records[8]=="O") or (records[3]==records[6]==records[9]=="O") or (records[1]==records[5]==records[9]=="O") or (records[3]==records[5]==records[7]=="O"):
        main_label.config(text="O wins")
        return True
    else:
        return False


def set_button_text(event: Event):
    if event.widget["state"]!="disabled":
        global turn
        button = event.widget
        button_number = str(button)[-1]
        if button_number == "n":
            button_number = "1"
        button_number = int(button_number)
        if button["text"] == "":
            button["text"] = turn
            records.update({button_number: turn})
            if turn == "X":
                turn = "O"
            elif turn == "O":
                turn = "X"
            set_label()
            if check_wnr():
                for widgets in buttons_frame.winfo_children():
                    widgets.configure(cnf={"state":"disabled"})


buttons_frame = Frame(master=appwin)
buttons_list=[]
for i in range(9):
    b = Button(master=buttons_frame, text="", font=("ink free", 20,"bold"), height=1, width=4, relief="groove",state="normal")
    buttons_list.append(b)
    b.grid(row=i//3, column=i % 3)
    b.bind("<Button-1>", func=set_button_text)
buttons_frame.pack()

Button(master=appwin, text="Restart", font=("ink free", 20, "bold"), relief="groove",command=reset_all).pack()

def set_label():
    main_label.config(text=f"{turn}'s turn")

appwin.mainloop()
