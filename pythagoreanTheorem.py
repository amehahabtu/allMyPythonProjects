# Pythagorean Theore Computation
def is_triangle(a,b,c):
    return a+b>c and a+b>c and b+c>a            
def is_rightangle_traingle(a,b,c):
    if not is_triangle(a,b,c):
        return False 
    if c > a and c > b:
        return c**2 == a**2 + b**2 
    if b > a and b > c:
        return b**2 == a**2 + c**2
    if a > b and a > c :
        return a**2 == b**2 + c**2
print(is_rightangle_traingle(5,3,4))
print(is_rightangle_traingle(1,3,4))