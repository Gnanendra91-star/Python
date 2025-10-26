#Add Elements: Add elements to the list.
list=[10,20]
a=40

list.append(a)
print(list)
#Remove Elements: Remove specific elements from the list.
list.pop(2)#by index value
print(list)
list.remove(10)#by itemname
print(list)
#Sort Elements: Sort the list in ascending and descending order.
l=[5,8,9,15,30,89]
print(sorted(l))
#Find Minimum and Maximum: Find the minimum and maximum elements in thelist.
print("The minimum value is:",min(l))
print("The maximum value is:",max(l))
#Calculate Sum and Average
print("The sum is:",sum(l))
print("The average is :",((sum(l)/len(l))))
list.insert(2,[1,2])
print(list)
list.reverse()
print(list)
print(list[0][1])

output:
[10, 20, 40]
[10, 20]
[20]
[5, 8, 9, 15, 30, 89]
The minimum value is: 5
The maximum value is: 89
The sum is: 156
The average is : 26.0
[20, [1, 2]]
[[1, 2], 20]
2
