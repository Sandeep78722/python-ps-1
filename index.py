
number = 181147

str = str(181147)

sum_of_digits = 0
for digit in str:
    sum_of_digits += int(digit)


average_of_digits = sum_of_digits / len(str)


print("Sum of digits:", sum_of_digits)
print("Average of digits:", average_of_digits)