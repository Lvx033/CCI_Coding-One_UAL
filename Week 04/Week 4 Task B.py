# Week 4 Task-2


wordList = input("Please input a list of words separated with a space. ").split(" ")

for x in wordList:
    for y in wordList:
        if x == y:
            pass
        else:
            print(x, y)
            
