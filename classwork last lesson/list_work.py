import random

limit = 5
numbers = []

for i in range(0, limit):
    numbers.append(random.randint(-10,10))

print(numbers)

#print the max number in list

max = -11 # any out of bound in the random range
for i in range(0,limit):
    if numbers[i] > max:
        max = numbers[i]

print(f"the max is {max}")

# swap between first and last elements

first_element = numbers[0]
useful_length = len(numbers) - 1

numbers[0] = numbers[useful_length]
numbers[useful_length] = first_element

print(numbers)
# reverse the elements in the list

for i in range(0,(useful_length + 1) // 2 ):
    last_value = numbers[i]
    numbers[i] = numbers[useful_length - i]
    numbers[useful_length - i] = last_value
    
print(numbers)