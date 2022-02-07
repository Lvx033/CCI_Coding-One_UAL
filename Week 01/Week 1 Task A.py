#task1.py

while True:
    try:
        answer = float(input("What is your number?: "))
        if answer % 2 == 0:
            print("Your number is Even.")
        else:
            print("Your number is Odd.")
    except ValueError:
        print("That's not a number.")
