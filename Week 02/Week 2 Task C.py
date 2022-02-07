# Week2 Task-C



while True:
    try:
        # Split input by dividend and divisor
        dividend, divisor = input("Please enter an integer division equation with the / symbol. ").split("/")
        # Parse dividend and divisor into integers because they are strings
        dividend, divisor = int(dividend), int(divisor)

        # Make sure that divisor is not 0 because it will crash the computer.
        if(divisor == 0):
            print("Undefined. \n")

        else:
            # Declare string with dividend to print later
            string = str(dividend)

            # while loop until dividend is 0 or divisor is greater than the dividend
            while(dividend > 0 and divisor <= dividend):
                # Add on subtractions to the string
                string += "-" + str(divisor)
                dividend -= divisor

            # Print the string and the remainder of the dividend
            print(string, "=", dividend, "\n")


    except ValueError:
        # Any non-integer will print this message.
        print("That is not a division equation. Please try again.\n")
