''' 
Date: 4/4/2021
Pogrammer Name:  Ameha Habtu
Description: This program is developed for my beloved daughters Eldana age 6 , and Daniela age 4. 
It asks the user(palyer) name ,how many times the player wants to keep playing, it tells how many plays left.
It also informs the result for each play. In the next verision it will include the time spent duration on each play 
and total time spent, and #will have also many fun and useful features.# check TIE condition, get summary of games how many win , lose, tie.
'''
def rock_paper_scissor():    
    global tie,win,lose,counter,num_of_trials
    import random
    system_choice=random.choice(["R","P","S"])
    print()
    print(f'You have left with {counter} play(s).')   
    user_choice= input("Do you want Rock, Paper, or Scissors?\nEnter R for Rock, P for Paper, S for Scissors: ").upper()
    R,P,S='Rock','Paper','Scissors'
    if (system_choice == user_choice):
        print(f'It is TIE! You said {user_choice}, computer system had also {system_choice}.Keep Playing...')
        tie +=1        
    elif (user_choice== "R" and system_choice=="S" ):
        print(f'Congratulation {name} You WIN, you said {user_choice} whereas the system had {system_choice}') 
        win +=1
        # num_of_trials += 3         
        # print(f'You got 3 plays as a bonus.')                                               
    elif (user_choice== "P" and system_choice=="R" ):
        print(f'Congratulation {name} You WIN, you said {user_choice} whereas the system had {system_choice}') 
        win += 1
        # num_of_trials += 3   
        # print(f'You got 3 plays as a bonus.')  
    elif (user_choice== "S" and system_choice=="P" ):
        print(f'Congratulation {name} You WIN, you said {user_choice} whereas the system had {system_choice}') 
        win += 1
        # num_of_trials += 3   
        # print(f'You got 3 plays as a bonus.')  
    else:     
        print(f'Sorry {name} You LOSE, the system WINS , you said {user_choice} whereas the system had {system_choice}')
        lose +=1
def main():
    global name,counter,num_of_trials,tie,win,lose
    tie=0
    win=0
    lose=0 
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    name=input("Enter your name : ").title()    
    print(f'Welcome {name} to ROCK-PAPER-SCISSORS game!')
    num_of_trials=int(input("How many times you want to play? "))
    counter=num_of_trials
    for i in range(num_of_trials):
        rock_paper_scissor()
        counter -= 1
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Thank you for playing ROCK-PAPER-SCISSORS game in our gaming platform!")    
main()
def game_stat():
    print(f'Your Game Statistics\nYou played {num_of_trials} game(s)\n\tWin: {win} game(s)\n\tLose: {lose} game(s)\n\tTIE : {tie} game(s)')
game_stat()