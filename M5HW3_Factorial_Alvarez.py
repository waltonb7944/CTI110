# Have program ask for nonnegative integer and then use loop to calculate
# the factorial of that number. Then displa the factorial
# CTI-110 Factorial
# Brittani Alvarez
# 11/16/17

def main():
    
    
    # Declaring variable.

    number = 0

    # Get a positive number from user and create loop.
    # Have loop keep asking for positive number if negative number or 0 entered.

    while number <= 0:
        number = int(input('Enter a positive integer: '))

        print()

    # Calculating the factorial.
        factorial = 1
     
        for factor in range(1, number + 1):
            factorial *= factor
            
    # Display the factorial of the number entered.

    print ('the factorial of' , number, 'is', factorial)
    
        
main()
