def check_triangle(a, b, c):
    """
    This function takes three sides of a triangle as input and returns the type of triangle.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"

    if a == b or a == c or b == c:
        return "Isosceles"

    return "Scalene"

side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))

triangle_type = check_triangle(side1, side2, side3)

print("The triangle is:", triangle_type)
