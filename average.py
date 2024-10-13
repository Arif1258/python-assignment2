def calculate_average(marks):
    """
    This function takes a list of marks as input and returns the average marks.
    """
    return sum(marks) / len(marks)

def calculate_grade(average_marks):
    """
    This function takes the average marks as input and returns the grade.
    """
    if average_marks >= 75:
        return 'A'
    elif average_marks >= 60 and average_marks <= 75:
        return 'B'
    elif average_marks >= 40 and average_marks <= 60:
        return 'C'
    else:
        return 'D'

marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))
marks4 = float(input("Enter marks in subject 4: "))

average_marks = calculate_average([marks1, marks2, marks3, marks4])

grade = calculate_grade(average_marks)

print("Average marks:", average_marks)
print("Grade:", grade)
