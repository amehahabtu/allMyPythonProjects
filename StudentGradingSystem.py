# This program accepts inputs(number of students,student's name , and three scores) from users and return the average mark and grade scored.
students=[]
while(True):
    try:
        num_students=int(input("How many number of students do you have? "))
        if num_students<0:
            print("Oops! You have entered negative number.Please re-enter: ")
            flag=False
        else :
            flag=True
            break
    except:
        print("Error! You have entered invalid input.Please re-enter.")
        flag=True
        continue
for i in range(num_students):
    scores=[]
    while (True):
        try:
            name=input(f'Enter the name of student{str(i+1)}: ')
            if name.isalpha():
                students = students +[name]      # using append method as students.append(name)     
            flag=False
            break
        except:
            print("Error ! You have entered invalid name input.")
            flag=True
            continue
    for j in range(3):
        score=float(input(f'Enter score{str(j+1)} for {name}: '))
        while (score<0 or score>100):
            score=float(input("Oops!You have entered invalid mark.Please re-enter mark from 0 thru 100: "))
        scores =scores +[score]  # using append method as scores.append(score)   
        average=sum(scores)/3
    print(f'The average score is :{round(average)}')
    if 98<=average<=100:
        grade="A+"
    elif 95<=average<98:
        grade="A"
    elif 91<=average<95:
        grade="A-"
    elif 88<=average<91:
        grade="B+"
    elif 84<=average<88:
        grade="B"
    elif 80<=average<84:
        grade="B-"
    elif 75<=average<80:
        grade="C+"
    elif 70<=average<74:
        grade="C"
    elif 60<=average<70:
        grade="D"
    elif 0<=average<60:
        grade="NG"
    else:
        print("Error , you have entered invalid mark.It should be between 0 thru 100.")
    print(f'{name} has scored {grade}.')
print(f'Thank you for using the system ! You are DONE for {num_students} students.')