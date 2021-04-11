# fibonacci  1,2,3,5,8,13,21,----(x-1)+(x-2)
def fibonacci(n):
    if n < 1 :
        return None  
    if n < 3:
        return 1  
    elem_1 =elem_2=1
    the_sum=0
    for i in range(3,n+1):
        the_sum= elem_1+elem_2
        elem_1,elem_2=elem_2,the_sum
    return the_sum       
def main():    
    num_fibo =int(input("How many number of terms do you need to generate fibonacci ? "))
    for n in range(1,num_fibo+1):
        print(n,"->",fibonacci(n))
main()
