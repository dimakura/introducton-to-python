numbers = [10, 6, 2, 3, 9, 0, 5, 7, 1, 4, 8]

min = numbers[0]
max = numbers[0]

for number in numbers:
    if number < min:
        min = number
    if number > max:
        max = number

print(f"Min: {min}")
print(f"Max: {max}")
