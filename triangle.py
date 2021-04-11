# Check whether it is traingle or not
def is_a_triangle(a,b,c):
    return a+b>c and a+c>b and  b+c>a

def side_size_validation(s):
    while s<=0:
        s=float(input('Invalid Side Size ! Please enter size greater than 0: '))
    return s
def main():
    sides=[]
    for i in range(3):
        while (True):
            try:
                side = float(input(f'Enter the size of side{i+1}: '))
                side=side_size_validation(side)
                sides.append(side)
                flag=False
                break
            except:
                print("Error ! Invalid character entered.Pls re-enter: ")
                flag=True
                continue
    print(sides)
    result=is_a_triangle(sides[0],sides[1],sides[2])
    print(result)
answer="Y"
while(answer=="Y"):
    main()
    answer=input("Do you want to check more....? (Y/N) ").upper()
print("Thank you ! YOU ARE DONE.")

# def is_a_triangle(a,b,c):
#     if a+b<c or a+c<b or b+c<a :
#         return False
#     else :
#         return True