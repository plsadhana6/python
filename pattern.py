def display_pattern():
    n = 5  # The number of rows and columns
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()  # Move to the next line after printing 5 stars

# Call the function to display the pattern
display_pattern()
