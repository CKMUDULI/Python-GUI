from tkinter import *
from random import randint

class numGuessingGame:
    def __init__(self) -> None:
        self.initialize_game()

    def chk_guess(self,event):
        self.check_guess()

    def check_guess(self):
        self.attempts+=1
        if self.guess_box.get().isnumeric():
            self.user_guess=int(self.guess_box.get())
            self.guess_box.delete(0,END)
            if self.user_guess>100 or self.user_guess<1:
                self.main_label.config(text=f'"The number is actually between 1 to 100"\nAttempt : {self.attempts}\nGuess Again...')
            else:
                if self.user_guess<self.random_num:
                    self.main_label.config(text=f'"Too Low !!!"\nAttempt : {self.attempts}\nGuess Again...')
                elif self.user_guess>self.random_num:
                    self.main_label.config(text=f'"Too High !!!"\nAttempt : {self.attempts}\nGuess Again...')
                else:
                    self.show_results()
        else:
            self.guess_box.delete(0,END)
            self.main_label.config(text=f'"Please! Enter a valid NUMBER"\nAttempt : {self.attempts}\nGuess Again...')

    def show_results(self):
        self.game_frame.destroy()

        self.results_frame=LabelFrame(appwin,text="Results",font=("Ink free",15,"bold"),relief=RIDGE,bd=5)
        
        Label(self.results_frame,font=("Ink free",15,"bold"),text=f"Congratulations !!!\nYou guessed the number in {self.attempts-1} attempts.\n").pack()
        
        Button(self.results_frame,font=("Ink free",20,"bold"),text="PLAY AGAIN",relief=RIDGE,bd=5,padx=5,pady=5,command=self.play_game).pack(fill=BOTH,expand=1)
        
        Button(self.results_frame,font=("Ink free",20,"bold"),text="QUIT",command=appwin.destroy,relief=RIDGE,bd=5,padx=5,pady=5).pack(fill=BOTH,expand=1)
        
        self.results_frame.pack(fill="both",expand=1,padx=50,pady=120)



    def play_game(self):
        self.random_num=randint(1,100)
        self.attempts=1
        
        for widget in appwin.winfo_children():
            widget.destroy()
        
        self.game_frame=LabelFrame(appwin,text="Guess The Number",font=("Ink free",15,"bold"),relief=RIDGE,bd=5)
        
        self.main_label=Label(self.game_frame,font=("Ink free",15,"bold"))
        self.main_label.config(text=f'\nAttempt : {self.attempts}\n"Guess A Number between 1 to 100"')
        self.main_label.pack()
        
        self.guess_box=Entry(self.game_frame,font=("Ink free",15),relief=RIDGE,bd=5)
        self.guess_box.focus_set()
        self.guess_box.bind("<Return>",self.chk_guess)
        self.guess_box.pack(pady=15)
        
        Button(self.game_frame,font=("Ink free",15,"bold"),text="Submit",relief=RIDGE,bd=5,padx=10,command=self.check_guess).pack()
        self.game_frame.pack(fill="both",expand=1,padx=50,pady=120)


    def initialize_game(self):
        gameTitle.destroy()
        
        self.frame1=LabelFrame(appwin,text="Game Options",font=("Ink free",15,"bold"),relief=RIDGE,bd=5)
        
        Button(self.frame1,font=("Ink free",20,"bold"),text="PLAY",relief=RIDGE,bd=5,padx=5,pady=5,command=self.play_game).pack(fill=BOTH,expand=1,padx=20,pady=5)
        
        Button(self.frame1,font=("Ink free",20,"bold"),text="QUIT",command=appwin.destroy,relief=RIDGE,bd=5,padx=5,pady=5).pack(fill=BOTH,expand=1,padx=20,pady=25)
        
        self.frame1.pack(fill="both",expand=1,padx=50,pady=100)

if __name__=="__main__":
    appwin=Tk()
    appwin.geometry("500x500")
    appwin.title("Number Guessing Game")
    appwin.resizable(width=False,height=False)
    gameTitle=Label(appwin,font=("Ink free",50,"bold"),text="Number\nGuessing\nGame",bd=5,relief=RIDGE)
    gameTitle.pack(fill=BOTH,expand=1,padx=50,pady=90)
    appwin.after(2000,lambda:numGuessingGame())
    appwin.mainloop()