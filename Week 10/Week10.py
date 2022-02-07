# Week 10-Dice

import random


class dice():

    def __init__(self, sides, dice_num, roll_num):
        self.sides = sides
        self.dice_num = dice_num
        self.roll_num = roll_num

    def roll(self):
        """Roll the dice"""
        # initialise the list to store the results
        results = []
        # loop through the number of dice
        for i in range(self.dice_num):
            # initialise the result to 0
            result = 0
            # loop through the number of sides
            for j in range(self.sides):
                # generate a random number between 1 and the number of sides
                result += random.randint(1, self.sides)
            # append the result to the list
            results.append(result)
        # return the list of results
        return results

    def __str__(self):
        """Print the results"""
        # initialise the string to store the results
        result = ""
        # loop through the number of dice
        for i in range(self.dice_num):
            # append the result to the string
            result += str(self.roll()) + "\n"
        # return the string of results
        return result


def main():
    """Main function"""
    # initialise the number of sides
    sides = 0
    # initialise the number of dice
    dice_num = 0
    # initialise the number of times the dice are rolled
    roll_num = 0
    # initialise the dice object
    dice_obj = None
    # initialise the string to store the results
    result = ""
    # initialise the string to store the user input
    user_input = ""

    # loop until the user enters a valid number of sides
    while sides <= 0:
        # get the number of sides from the user
        sides = int(input("Please enter the number of sides on the dice: "))
        # if the number of sides is less than or equal to 0,
        # print an error message and ask for a number greater than 0
        if sides <= 0:
            print("The number of sides must be greater than 0")
            sides = 0

    # loop until the user enters a valid number of dice
    while dice_num <= 0:
        # get the number of dice from the user
        dice_num = int(input("Please enter the number of dice: "))
        # if the number of dice is less than or equal to 0,
        # print an error message and ask for a number greater than 0
        if dice_num <= 0:
            print("The number of dice must be greater than 0")
            dice_num = 0

    # loop until the user enters a valid number of times the dice are rolled
    while roll_num <= 0:
        # get the number of times the dice are rolled from the user
        roll_num = int(input("Please enter the number of times the dice are rolled: "))
        # if the number of times the dice are rolled is less than or equal to 0,
        # print an error message and ask for a number greater than 0
        if roll_num <= 0:
            print("The number of times the dice are rolled must be greater than 0")
            roll_num = 0

    # create the dice object
    dice_obj = dice(sides, dice_num, roll_num)

    # loop through the number of times the dice are rolled
    for i in range(roll_num):
        # append the result to the string
        result += str(dice_obj.roll()) + "\n"

    # print the results
    print(result)


if __name__ == "__main__":
    main()