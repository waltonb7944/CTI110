# Get 5 test scores and show the grade and then show the average grade.
# 11/10/17
# CTI-110 M6HW1 test average and grade
# Brittani Alvarez

# calc_average function should accept five test scores (int or float) as
# arguemnets, and return the average of the scores.

# (in order to calculate an average, you should take the total of all grades
# and then divide it be the number of grades.

# determine_grade should accept a test score (int or float) as an arguement
# and return a letter grade for the score use 10 point grading scale
# the letter grade should be a, b, c... and string



def calc_average(num1,num2,num3,num4,num5):
    return (num1+num2+num3+num4+num5)/5

def determine_grade(num):
    if(num>=90 and num<=100):
        return "A"
    if(num>=80 and num<=89):
        return "B"
    if(num>=70 and num<=79):
        return "C"
    if(num>=60 and num<=69):
        return "D"
    if(num<60):
        return "F"


def main():
    marks1=int(input("Enter 1st test score "))
    marks2=int(input("Enter 2nd test score "))
    marks3=int(input("Enter 3rd test score "))
    marks4=int(input("Enter 4th test score "))
    marks5=int(input("Enter 5th test score "))
    print("Score Grade")
    print(marks1,determine_grade(marks1))
    print(marks2,determine_grade(marks2))
    print(marks3,determine_grade(marks3))
    print(marks4,determine_grade(marks4))
    print(marks5,determine_grade(marks5))
    print("The average of all test score is : ",calc_average(marks1,marks2,marks3,marks4,marks5))

main ()
