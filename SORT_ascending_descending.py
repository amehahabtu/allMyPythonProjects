
def sort_in_ascending_order():
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(numbers)-1):        
            if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped=True
    print(f'Numbers after sorted in ascending order :\n',numbers)
    #print(f'Top three numbers: {numbers[0:3]}')
def sort_in_descending_order():    
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(numbers)-1):      
            if numbers[i] < numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped=True
    print(f'Numbers after sorted in descending order :\n',numbers)
    #print(f'Top three numbers: {numbers[0:3]}')
def main():  
    global numbers
    numbers=[]
    num_size=int(input("Enter the number size: "))
    for i in range(num_size):
        number=int(input(f'Enter a number{str(i+1)}: '))
        numbers.append(number)
    print(f'Numbers before sorted:\n',numbers)
    sort_in_ascending_order()
    sort_in_descending_order()
main()