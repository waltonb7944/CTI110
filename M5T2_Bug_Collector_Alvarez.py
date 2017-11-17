# Needs to calculate a running total of number of bugs collected over 7 days.
# CTI-110 Bug Collector
# Brittani Alvarez
# 11/15/17



# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
