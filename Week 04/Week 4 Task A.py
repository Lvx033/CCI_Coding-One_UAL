#Week 4 Task-1

inputList = input("Please enter a list of numbers, separating them with a space.\n").split(" ")
numList = [ x for x in inputList if x.isdigit() ]

product = 1
string = ""
for num in numList:
    product = product * int(num)
    if numList.index(num) == len(numList)-1:
        string = string + num + "="
    else:
        string = string + num + "*"
print(string + str(product)) 
