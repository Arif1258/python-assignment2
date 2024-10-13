def find_largest(a, b, c):
    """
    This function takes three numbers as input and returns the largest among them.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

largest_num = find_largest(num1, num2, num3)

print("The largest number is:", largest_num)
