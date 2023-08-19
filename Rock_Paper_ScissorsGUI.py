#Rock Paper Scissors
import random
import time
import tkinter as tk 

#1 == Scissors

#2 == Paper

#3 == Rock

Objects = None
res = None
lose = 0
win = 0
tie = 0
####Functions####

def rock():
    global Objects
    Objects = "Rock"
    PlayerSelect.config(text=f"Object Selected: ({Objects})")
     


def paper():
    global Objects
    Objects = "Paper"
    PlayerSelect.config(text=f"Object Selected: ({Objects})")
   
      


def scissors():
    global Objects
    Objects = "Scissors"
    PlayerSelect.config(text=f"Object Selected: ({Objects})")


def Clear():
    global Objects
    global res
    global win
    global lose

    Objects = None
    res = None
    PlayerSelect.config(text="Object Selected: ()")
    Result2.config(text=f"{res}")
    Result.config(text="Computer: ()")



def Go():
    global Objects
    global res
    global win
    global lose
    global tie
    
    if Objects != "Scissors" and Objects != "Paper" and Objects != "Rock":
        PlayerSelect.config(text=f"Object Selected: ({Objects})")
        Result.config(text=f"Computer: (None)")
        Result.place(x=520, y=400)
        res = None
        Result2.config(text=f"{res}")
   
    else:
        randomNum = random.randint(1,3)
        
        if randomNum == 1:

            Result.config(text="Computer: (Scissors)")
            Result.place(x=465,y=400)

            if Objects == "Scissors":
                res = "Tie!"
                Result2.config(text=f"{res}")
                tie+=1
                Tie.config(text=f"Ties: {tie}")

            elif Objects == "Paper":
                res = "You Lose!"
                lose+=1
                Lose.config(text=f"Loses: {lose}") 
                Result2.config(text=f"{res}")

            elif Objects == "Rock":
                res = "You Win!"
                win+=1
                Result2.config(text=f"{res}")
                Win.config(text=f"Wins: {win}")    

        if  randomNum == 2:
            Result.config(text="Computer: (Paper)")
            Result.place(x=510,y=400)
            if Objects == "Scissors":
                res = "You Win!"
                win+=1
                Result2.config(text=f"{res}")
                Win.config(text=f"Wins: {win}")    

            elif Objects == "Paper":
                res = "Tie!"
                Result2.config(text=f"{res}")
                tie+=1
                Tie.config(text=f"Ties: {tie}")

            elif Objects == "Rock":
                res = "You Lose!"
                lose+=1
                Lose.config(text=f"Loses: {lose}")
                Result2.config(text=f"{res}") 
    
        if randomNum == 3:
            Result.config(text="Computer: (Rock)")
            Result.place(x=520,y=400)
            if Objects == "Scissors":
                res = "You Lose!"
                lose+=1
                Lose.config(text=f"Loses: {lose}")
                Result2.config(text=f"{res}")

            elif Objects == "Paper":
                res = "You Win!"
                win+=1
                Result2.config(text=f"{res}")
                Win.config(text=f"Wins: {win}")    

            elif Objects == "Rock":
                res = "Tie!"
                Result2.config(text=f"{res}")
                tie+=1
                Tie.config(text=f"Ties: {tie}") 
    
#####################





window = tk.Tk()
window.title("Rock, Paper, Scissors by CoolMetDuck")
window.geometry("800x500")
window.configure(bg='#C3C4C1')

Title = tk.Label(window, text="Rock, Paper, Scissors by CoolMetDuck", font=("Helvetica", 20, "bold"), bg="#C3C4C1")
Title.pack()


PlayerSelect = tk.Label(window, text="Object Selected: ()", font=("Helvetica", 24, "bold"), bg="#C3C4C1")
PlayerSelect.place(x=20,y=400)

Result = tk.Label(window, text="Computer: ()", font=("Helvetica", 24, "bold"), bg="#C3C4C1")
Result.place(x=600, y=400)

Result2 = tk.Label(window, text=f"{res}", font=("Helvetica", 24, "bold"), bg="#C3C4C1")
Result2.place(x=370, y=355)

Win = tk.Label(window, text=f"Wins: {win}", font=("Helvetica", 18, "bold"), bg="#C3C4C1")
Win.place(x=2,y=140)

Lose = tk.Label(window, text=f"Loses: {lose}", font=("Helvetica", 18, "bold"), bg="#C3C4C1")
Lose.place(x=2,y=190)

Tie = tk.Label(window, text=f"Ties: {tie}", font=("Helvetica", 18, "bold"), bg="#C3C4C1")
Tie.place(x=2,y=240)


Rock = tk.Button(window, text="Rock", font=("Helvetica", 35), command=rock ,  height=1, width=5, cursor="hand2")
Rock.place(x = 150, y = 100)

Paper = tk.Button(window, text="Paper", font=("Helvetica", 35), command=paper ,  height=1, width=5, cursor="hand2")
Paper.place(x= 350, y= 100)

Scissors = tk.Button(window, text="Scissors", font=("Helvetica", 35), command=scissors ,  height=1, width=7, cursor="hand2")
Scissors.place(x=550, y= 100)

GoButton = tk.Button(window, text="Go!", font=("Helvetica", 35), command=Go, height=1, width=4, cursor="hand2", bg="#2DF41C")
GoButton.place(x=350,y=250)

ClearButton = tk.Button(window,text="Clear",font=("Helvetica", 25), command=Clear, height=1, width=5, cursor="hand2", bg="#FF2200")
ClearButton.place(x=30,y=300)

window.mainloop()