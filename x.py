def display_x_pattern():
    n = 5  # The size of the grid (5x5)
    for i in range(n):
        for j in range(n):
            # Print a star if the current position is on either diagonal
            if i == j or i + j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # Move to the next line after printing each row

# Call the function to display the pattern
display_x_pattern()
