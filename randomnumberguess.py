from random import randint
#num_try=int(input("Enter your number of trials: "))
#counter=0
def randomnumberguess():      
    while(True):        
        try:
            print()
            print('++++++++++++++++++++++++GUESS NUMBER GAME++++++++++++++++++++++++++++++++++++++')
            num=int(input("Please enter number you want to win between 0-10: ")) 
            #counter += counter            
            #inputvalidation(num)
            #number=num
            flag=False
            break
        except:
            print("Oops! You have entered invalid number!")
            flag=True
            continue 
    if num==randint(0,10):
        #print(randint(1,10))
        print(f'Congratulation ! You win $ 1,000,000.00 !')       
    else :
        print("Sorry You lose ! Please try more")
        randomnumberguess()
randomnumberguess()

def inputvalidation(number):
    while(0<=number<=10):
        nummber=int(input("Enter your number: "))
    return number 
    
# ans="Y"
# while (ans=="Y"):   
    
#     ans=input("Do you to try more..? (Y/N)").upper()
# print('You are DONE. BYE!!!')
    
