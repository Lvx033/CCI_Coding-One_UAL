# Week 5 Task-B (Caesar Cipher)



word = input("Enter a string to enrypt: ")
shift = int(input("Enter a shift amount: "))

for letter in word.lower():
    if letter.isalpha():
        value = ord(letter) + shift
        if value > 122:
            value = value - 26
        print(chr(value), end="")
    else:
        print(letter, end="")
print()
    
