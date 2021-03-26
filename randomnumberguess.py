from random import randint
ans="Y"
while (ans=="Y"):   
    while(True):
        try:
            num=int(input("Please enter number you want to win between 1-10: ")) 
            flag=False
            break
        except:
            print("Oops! You have entered invalid number!")
            flag=True
            continue 
    if num==randint(0,10):
        #print(randint(1,10))
        print("Congratulation ! You win $ 1,000,000.00 !!!")
    else :
        print("Sorry You lose !")
    ans=input("Do you to try more..? (Y/N)").upper()
print('You are DONE. BYE!!!')
    

