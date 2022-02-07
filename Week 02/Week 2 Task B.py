# Week2 Task-B



string = input("Enter your text. ")

#Lowercase text
string = string.lower()
# Remove all spaces & non-alphabetical chart
string = ''.join([i for i in string if i.isalpha()])


alphabet = [0] * 26

# Loop through the letters in the string
for x in string:

    letter = ord(x) - 97
    # Add 1 to each corresponding letter
    alphabet[letter] = alphabet[letter] + 1

# For loop to print each letter 
for x in range(0,26):
    print(str(chr(97+x)) + ": " + str(alphabet[x]))
