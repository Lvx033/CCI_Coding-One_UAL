# Week2 Task-A



while True:
    try:
        # Declare variable "sum" and set it equal to 0
        sum =  0
        # Declare input with three different variables, x, y, z
        # Separate input by space
        x, y, z = input("Please input three positive integers separated with a space. ").split(" ")
        # Parse the input into integers because they are strings
        x, y, z = int(x), int(y), int(z)

        # Initiate for loop between x and y
        for i in range(x, y):

            if z % i == 0:
                print(i, "is a multiple of", z)
                sum =  sum + i

        print("The sum of all numbers bewtween the first two that are a multiple of the third is:", sum, "\n")


    except ValueError:
        print("That is not a number.\n")
