# Ask for a positive number and keep on looping until a negative number is 
# entered. It will end when negative number is entered and show total.
# CTI-110 M5HW2 Running Total
# Brittani Alvarez
# 11/17/17



def main():
    
    
    # declaring and initializing variables.

    number = 1.0
    runningTotal = 0.0

    # Loop to add numbers until a negative one is entered.

    while number >= 0:
        number = float(input('Enter a number: '))

    # Check to see if number is positive and if it is add it to running total.
    # If number is neative end the loop and do not add that number to running total.
    
        if number >= 0:
            runningTotal = runningTotal + number
            print()
            
    # Display the running total.

    print()
    print ('Total = ' , format(runningTotal, '.2f'))
    
        
main()
