#Rock Paper Scissors
import random
import time


##3 == scissors

##2 == Paper

#1 == Rock

Win = 0

Lose = 0

Tie = 0
while True:
    Player = input('\n\n  Welcome to Rock Paper Scissors by CoolMetDuck! \n\n Choose which move to play!\n\n 1. Rock("Rock")\n\n 2. Paper("Paper") \n\n 3. Scissors ("Scissors")\n\n  \n4. Stats ("Stats")\n\n').lower().strip()

    if Player == 'rock':
        random_NUM = random.randint(1, 3)
        time.sleep(2)
        if random_NUM == 1:
            Tie+=1
            print("\n\n(Rock)Tie! Computer chose rock!\n\n")

        elif random_NUM == 2:
            Lose+=1
            print("\n\n(Rock) You lose! Computer chose paper!\n\n")

        elif random_NUM == 3:
            Win+=1
            print("\n\n(Rock) You win! Computer chose scissors!\n\n")    
    

    elif Player == 'paper':
        random_NUM = random.randint(1, 3)
        time.sleep(2)
        if random_NUM == 1:
            Win+=1
            print("\n\n(Paper) You win! Computer chose rock!\n\n")

        elif random_NUM == 2:
            Tie+=1
            print("\n\n(Paper) Tie! Computer chose paper!\n\n")


        elif random_NUM == 3:
            Lose+=1
            print("\n\n(Paper) You lose! Computer chose scissors!\n\n")                
    
    elif Player == 'scissors':
        random_NUM = random.randint(1, 3)
        time.sleep(2)
        if random_NUM == 1:
            print("\n\n(Scissors) You lose! Computer chose rock!\n\n")
            Lose+=1

        elif random_NUM == 2:
            print("\n\n(Scissors) You win! Computer chose paper!\n\n")
            Win+=1

        elif random_NUM == 3:
            print("\n\n(Scissors) Tie! Computer chose scissors")
            Tie+=1        

    elif Player =="stats":
        print(f"\n\n ********Stats********\n\n  Wins: ({Win})\n\n Loses: ({Lose})\n\nTies: ({Tie})") 
    else:
        time.sleep(2)
        print("Invalid Input! Try again!")