
# CTI-110
# M6T1- Kilometer Converter
# Brittani Alvarez
# 11/04/2017

# Write a program that gets kilometers and converts it to miles



CONVERSION_FACTOR = 0.6214

def main ():
    # Get the distance in kilometers.
    kilometers = float(input("Enter a distance in kilometers: "))

    show_miles(kilometers)

def show_miles(km):
    # convert to miles
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print (km, 'kilometers equals', miles, 'miles.')

#call the main function
main ()
