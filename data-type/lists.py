list_1 = [1, 2, 3, "Hi", 3j]

list_1.append('Bye')
list_1.append('Ciao')

list_2 = list_1.copy()
print(list_1)
#Clear list
list_1.clear()

print(list_1, list_2)

print(f'Number 2 appears {list_2.count(2)} time in list')

list_2.append(3)
#Length of list
print(len(list_2))


# Index and elements
print(list_2[0])

# Delete elements

names = ['Daniel', 'Arthur', 'James', 'Abram']

print(names)
names.pop() # Delete last element

names.remove('Arthur') # Delete element by value

print(names)

# Reverse and Sort

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
