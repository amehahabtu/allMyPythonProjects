print()
print("Welcome to ABC coffee vending machine! Here are our coffee menu:\n1.Espresso (Small $1.75 , Medium $3.50, Large $5.25)\n2.Americano (Small $1.75 , Medium $3.50, Large $5.25)\n3.Café au Lait (Small $1.75 , Medium $3.50, Large $5.25)\n4.Latte (Small $1.75 , Medium $3.50, Large $5.25)\n5.Cappuccino (Small $1.75 , Medium $3.50, Large $5.25)\n6.Macchiato (Small $1.75 , Medium $3.50, Large $5.25)\n7.Mocha (Small $1.75 , Medium $3.50, Large $5.25)")
print()
coffee_price=1.75 # price for small coffee size , it will be basis for other sizes M and L.
choice_selected=int(input("Please enter your coffee choice number: "))
if (1 <= choice_selected <=7):
    if (choice_selected == 1 ):
        print("You have selected Expresso Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large")    
    elif (choice_selected == 2):
        print("You have selected Americano Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large")       
    elif (choice_selected == 3):
        print("You have selected Cafe au Lait Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large")    
    elif (choice_selected == 4):
        print("You have selected Latte Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large")   
    elif (choice_selected == 5):
        print("You have selected Cappucino Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large") 
    elif (choice_selected == 6):
        print("You have selected Macchiato Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large")      
    else:
        print("You have selected Mocha Coffee.Here are list of coffee drink sizes.\nCoffee-SmallSize(9oz)\nCoffee-MediumSize(12oz)\nCoffee-LargeSize(15oz)\nYou can enter letter s or S for Small, m or M for Medium ,l or L for Large")   
else :
    print("Error ! You have selected wrong choice.Please selecte from 1 thru 7.")
    exit()
size_selected=input("Please enter the size: ").upper()
if (size_selected =='S'):
    coffee_price=coffee_price
    print("You have ordered coffee with small size.It's price is $",coffee_price)
elif (size_selected =='M'):
    coffee_price *= 2
    print("You have ordered coffee with medium size.It's price is $",coffee_price)
elif (size_selected =='L'):
    coffee_price *= 3
    print("You have ordered coffee with large size.It's price is $",coffee_price)
else :
    print("You have entered invalid coffee size.")  
    exit()
payment_received = float(input("Please insert cash for the payment : "))
if (payment_received > 0):    
    if (payment_received == coffee_price) :
        print("You have paid $",payment_received,'.Thank You Enjoy Your Coffee!')
    elif (payment_received < coffee_price) :
        print("Sorry, the amount you paid $",payment_received,"is insuffient amount to buy the item.You need to insert additional $",coffee_price-payment_received)
    else:
        print("You have paid $",payment_received,".You have change due $",payment_received-coffee_price,'.Thank you Enjoy Your Coffee!')
else :
    print("Error! You have entered invalid input.")