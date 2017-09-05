
# CTI-110
# M2HW2 - Tip Tax Total
# Brittani Alvarez
# 09/04/2017

# Write a program that calculates the totl cost of a meal purchased at a restaurant


# Get the user to input the total cost of the meal.
foodCost = float(input ("Enter the total cost of the meal: "))


#Calculate the amount of the tip at 18% and the sales tax at 7%

tipAmount = foodCost * .18
salesTax = foodCost * .07

# Get the total cost of the meal. With the adding food cost, tip and tax together.

totalCost = foodCost + tipAmount + salesTax

# Diplay the tip, tax and total cost of the food.

print ('The cost of the tip is $', format(tipAmount, ',.2f'))
print ('The cost of the sales tax is $', format(salesTax, ',.2f'))
print ('The total cost of the meal is $', format(totalCost, ',.2f'))
