# Factorial numbers ---n!=1*2*3*4*--------(n-1)*n
def factorial(n):
    if n < 0 :
        return False
    if n <2 :
        return 1
    product =1
    for i in range(2,n+1):
        product *= i
    return product
def main():
    num=int(input("Enter the number to be factored: "))
    for n in range(1,num):
        print(n, "->",factorial(n))
main()

# factorial using recursive function 
def factorial_recursive(n):
    if n < 0 :
        return False
    if n <2 :
        return 1
    return n*factorial_recursive(n-1)
def other_main():
    num=int(input("Enter the number to be factored: "))
    for n in range(1,num):
        print(n, "->",factorial_recursive(n))
other_main()

  
