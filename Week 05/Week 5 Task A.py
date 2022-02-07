# Week 5 Task A (NATO).py



table = {
    "a" : "alpha",
    "b" : "bravo",
    "c" : "charlie",
    "d" : "delta",
    "e" : "echo",
    "f" : "foxtrot",
    "g" : "golf",
    "h" : "hotel",
    "i" : "india",
    "j" : "juliett",
    "k" : "kilo",
    "l" : "lima",
    "m" : "mike",
    "n" : "november",
    "o" : "oscar",
    "p" : "papa",
    "q" : "quebec",
    "r" : "romeo", 
    "s" : "sierra",
    "t" : "tango",
    "u" : "uniform",
    "v" : "victor",
    "w" : "whiskey",
    "x" : "x-ray",
    "y" : "yankee",
    "z" : "zulu",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "0" : "zero"
}

word = input("Enter your word. ")
for x in word.lower():
    if x in table:
        print(table[x], end=" " + "\n")

print()

def get_key(val):
    for key, value in table.items():
         if val == value:
             return key
 
    return "Key doesn't exist. "

convert = input("Enter the NATO phonetic alphabet to convert into a word, separating with a space. ").split(" ")
for x in convert:
    print(get_key(x), end="")
print()
