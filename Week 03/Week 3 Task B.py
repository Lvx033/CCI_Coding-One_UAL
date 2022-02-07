# Week 3

sentence = input("Please enter your string of text to convert to Pig Latin: ").split(" ")
text = ""
for string in sentence:
    if(string[0] in {"a", "e", "i", "o", "u"}):
        string = string + "yay"
        text = text + string + " "
    elif(string[1] in {"a", "e", "i", "o", "u"}):
        string = string[1:len(string)] + string[0] + "ay"
        text = text + string + " "
    else:
        x=0
        for letter in string:
            if letter in  {"a", "e", "i", "o", "u"}:
                string = string[x:len(string)] + string[:x] + "ay"
                text = text + string + " "
                break
            else:
                x += 1
print("Converted text: " + text)
