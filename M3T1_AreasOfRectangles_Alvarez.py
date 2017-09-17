
# CTI-110
# M3T1-Areas Of Rectangles
# Brittani Alvarez
# 9/15/2017

# Write a program that asks for the length and width of two rectangles.


# Get the length and width of rectangle 1.
length1 = int(input('Enter the length of rectangle 1:'))
width1 = int(input('Enter the width of rectangle 2:'))


# Get the length and width of rectangle 2.
length2 = int(input('Enter the length of rectangle 2:'))
width2 = int(input('Enter the width of rectangle 2:'))


# Calculate the areas of the 2 rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which rectangle's area is greater
# Using an If-elif-else statement

if area1 > area2:
    print ('Rectangle 1 has the greater area.')
elif area2 > area1:
    print ('Rectangle 2 has the greater area.')
else:
    print ('Both rectangles have the same area.')
