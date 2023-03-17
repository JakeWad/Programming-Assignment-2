def tower(n):
    # calculate total height of the tower
    height = (2 * n) + 2

    # loop through each level of the tower
    for i in range(height):
        # check if the current level is the base of the tower
        if i == height - 2:
            # print the base of the tower
            print('/' + ('_' * (2 * n)) + '\\')
        else:
            # calculate the number of spaces and stars to print
            spaces = (height - i - 3)
            stars = 2 * (i // 2) + 2

            # print the spaces and stars
            print((' ' * spaces) + ('*' * stars) + (' ' * spaces))

tower(1)
print('\n')
tower(2)
print('\n')
tower(3)
