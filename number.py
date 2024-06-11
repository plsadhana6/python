def display_number_pattern():
    n = 5  # The starting number of the pattern
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()  # Move to the next line after printing each row

# Call the function to display the pattern
display_number_pattern()
