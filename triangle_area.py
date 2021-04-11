# a = (b*h)/2  s = (a+b+c)/2
# heron's formula  a= (s(s-a)(s-b)(s-c))**0.5

def is_triangle(a,b,c):
    return a+b>c and a+b>c and b+c>a    
def heron(a,b,c):
    s=(a+b+c)/2
    return (s*(s-b)*(s-b)*(s-c))**0.5
def area_of_triangle(a,b,c):
    if not is_triangle(a,b,c):
        return False
    return heron(a,b,c)
print(area_of_triangle(1.,1.,2.**.5))