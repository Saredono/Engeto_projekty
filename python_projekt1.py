"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Golasowski
email: golasowski.tomas@gmail.com
discord: Tomáš G.
"""
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


separator = "-" * 30
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
sentence =  "LEN   |   OCCURENCES  |   NR."

username = input("username: ")
password = input("password: ")

if users.get(username) == password:
    print(separator,f"Welcome to the app, {username}\n"
      "We have 3 texts to be analyzed",separator, sep="\n")
    
else:
    print("Unregistered user, terminating program...")
    quit()
    
text = input("Enter a number btw. 1 and 3 to select: ")

if not text.isnumeric():
    print("Incorrect data, terminating program...")
    quit()

elif 1 <= int(text) <= 3:
    selected_text = TEXTS[int(text) - 1]

else:
    print("Incorrect data, terminating program...")
    quit()


print(separator, selected_text, separator, sep="\n")


splitted_text = selected_text.split()

#ČISTÝ TEXT BEZ ZNAKŮ: 

clean_text = [word.strip(",.") for word in splitted_text]

count = len(clean_text)
title = 0
upper = 0
lower = 0
numeric = 0

for word in clean_text:
    if word.istitle():
        title += 1
    elif word.isupper():
        upper += 1
    elif word.islower():
        lower += 1
    elif word.isnumeric():
        numeric += 1

print(f"There are {count} words in the selected text.")
print(f"There are {title} titlecase words.")
print(f"There are {upper} uppercase words.")
print(f"There are {lower} lowercase words.")
print(f"There are {numeric} numeric strings.")

sumary = [int(word) for word in clean_text if word.isnumeric()]

sumary_total = sum(sumary)

print(f"The sum of all the numbers: {sumary_total}.")


print(separator, sentence, separator, sep="\n")


length = [len(word) for word in clean_text]

sorted_length = length.sort()

count_length = {}


for number in length:
    if number not in count_length:
        count_length[number] = 1
    else:
        count_length[number] += 1


for number,stars in count_length.items():
    print(f"{str(number):>5} | {('*' * stars):<13} | {str(stars)}")