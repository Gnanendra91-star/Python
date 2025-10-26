tuple=(10, 'hello', 3.14, 'world')
print(tuple)
#Access Elements: Access individual elements and slices of the tuple.
for i in tuple:
    print(i)
print(tuple[1:3])
print(tuple[:-1])
#Concatenate Tuples: Combine two tuples to create a new tuple.
t2=(5,0.5)
t3=tuple+t2
print(t3)
# Tuple Unpacking
a, b, c, d = tuple
print(f"Unpacked Values: a={a}, b={b}, c={c}, d={d}")
#Membership Testing
print("Is 'hello' in tuple?", 'hello' in tuple)
#Tuple Length
print("Length of Tuple:", len(tuple))
# Using functions where applicable
numeric_tuple = (5, 10, 15)
print("Max:", max(numeric_tuple))
print("Min:", min(numeric_tuple))
print("Sum:", sum(numeric_tuple))
tuple(3)="PI" 

output:
(10, 'hello', 3.14, 'world')
10
hello
3.14
world
('hello', 3.14)
(10, 'hello', 3.14)
(10, 'hello', 3.14, 'world', 5, 0.5)
Unpacked Values: a=10, b=hello, c=3.14, d=world
Is 'hello' in tuple? True
Length of Tuple: 4
Max: 15
Min: 5
Sum: 30
File "/tmp/ipython-input-1581457055.py", line 1
    tuple(3)="PI" #ERROR
    ^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
