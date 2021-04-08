
#--------------------Total with and without using sum() function-------------------------------------------------------------------------------
my_list=[10,1,8,3,5]
print("Total using sum function: ",sum(my_list))
total=0
for i in my_list:
    total +=i
print("Total without sum() function: ",total)
#----------------------Max with and without using max() function---------------------------------------------------------------------------
my_list=[11,222,-3,4,50]

print(f'Maximum num using max()function: ',max(my_list))
max_num = my_list[0]
for i in range(len(my_list)):  
    if my_list[i] > max_num:
        max_num = my_list[i]
print("The maximum number  without max() is :",max_num)
#----------------------Min with and without using min() function-----------------------------------------------------------------------------
my_list=[11,222,-3,4,50]
print(f'Minimum num using min()function: ',min(my_list))
min_num=my_list[0]
for i in range(len(my_list)):   
    if my_list[i] < min_num:
        min_num=my_list[i]
print('The minimum number without min() is :',min_num)    

#-------------sorting ascending and descending without using built in function ????/------------------------------

my_list=[8,10,6,2,4]
print('before sorted',my_list)
swapped=True 
while swapped:  
    swapped=False
    for i in range(len(my_list)-1):
        if my_list[i]>my_list[i+1]:
            swapped=True
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
print('after sorted in ascending order: ',my_list)

my_list=[8,10,6,2,4]
print('before sorted',my_list)
swapped=True 
while swapped:  
    swapped=False
    for i in range(len(my_list)-1):
        if my_list[i] < my_list[i+1]:
            swapped=True
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
print('after sorted in descending order: ',my_list)