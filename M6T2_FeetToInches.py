
# Converting feet to inches
# 11/10/17
# M6T2_FeetToInches
# Brittani Alvarez


# Global constant
INCHES_PER_FOOT = 12

#main function
def main():
    #Get the number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# Function
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main ()
