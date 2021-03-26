import random
numbers=[0,1,2,3,4,5,6,7,8,9]
def generatelottolucknum(): 
    lotterylucknum=[]  
    length_lottonum=len(numbers)-1
    for i in range(5):
        indexnum=random.randint(0,length_lottonum)
        lotterylucknum.append(numbers[indexnum])
    return lotterylucknum
print()
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(f'The lucky lotto number is: {generatelottolucknum()}')   