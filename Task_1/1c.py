import math
 # Function to find distance
def distance(x1, y1, z1, x2, y2, z2):
     d = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) +
                math.pow(z2 - z1, 2)* 1.0)
    print("Distance is ")
    print(d)
 # Driver Code	
x1 = float(input("Enter the X1-coordinate: "))
y1 = float(input("Enter the Y1-coordinate: "))
z1 = float(input("Enter the Z1-coordinate: "))
x2 = float(input("Enter the X2-coordinate: "))
y2 = float(input("Enter the Y2-coordinate: "))
z2 = float(input("Enter the Z2-coordinate: "))
# function call for distance
distance(x1, y1, z1, x2, y2, z2)   

output:
Enter the X1-coordinate: 4
Enter the Y1-coordinate: -2
Enter the Z1-coordinate: 3
Enter the X2-coordinate: 7
Enter the Y2-coordinate: 2
Enter the Z2-coordinate: -5
Distance is 
9.433981132056603
