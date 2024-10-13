num = int(input("Enter a number: "))

sum_of_digits = 0

while num:
    sum_of_digits += num % 10
    num //= 10

print("The sum of digits is", sum_of_digits)
