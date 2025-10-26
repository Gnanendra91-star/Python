import math 
def equationroots( x, y, z): 
    discri = y * y - 4 * x * z 
    sqrtval = math.sqrt(abs(discri))   

    # checking condition for discriminant
    if discri > 0: 
        print(" real and different roots ") 
        print((-y + sqrtval)/(2 * x)) 
        print((-y - sqrtval)/(2 * x))   

    elif discri == 0: 
        print(" real and same roots") 
        print(-y / (2 * x))   

    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- y / (2 * x), " + i", sqrtval) 
        print(- y / (2 * x), " - i", sqrtval) 

# Driver Program 
x = int(input())
y = int(input())
z = int(input())
if x == 0: 
        print("Input correct quadratic equation")
else:
    equationroots(x, y, z)

output:
2
-1
3
Complex Roots
0.25  + i 4.795831523312719
0.25  - i 4.795831523312719
