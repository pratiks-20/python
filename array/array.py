import array

numbers = array.array('i', [1, 2, 3, 4, 5])

print("Array elements:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers[2] = 10
print("Modified array:", numbers)

print("Array elements one by one:")
for num in numbers:
    print(num)
