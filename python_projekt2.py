"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tomáš Golasowski
email: golasowski.tomas@gmail.com
discord: Tomáš G.
"""

import random
import time


separator = 30 * "-"

user = input("Enter your name: ")
print("Hello,", user)

print(separator, "I've generated a random 4 digit number for you." "\n"
      "Let's play a bulls and cows game.", separator, sep="\n")


def generate_number():

    """ vytvoří náhodné 4 místné číslo s unikátními číslicemi,
        které nezačíná 0"""

    random_number_list = [0]
    while random_number_list[0] == 0:
        random_number_list = random.sample(range(10), 4)

    return random_number_list

def get_guess():

    """od uživatele získá číslo, které musí splňovat určité podmínky"""

    while True:
        guess_number = input("Guess the 4 digit number (or type 'exit' to quit): ")

        if guess_number.lower() == "exit":
            quit()
        elif len(guess_number) != 4:
            print("Your guess must be exactly 4 digits long. Try again.")
        elif not guess_number.isnumeric():
            print("You've entered wrong input, try again")
        else:
            print(separator, "\n"
                  "Your Guess:", guess_number)
            number_list = [int(i) for i in guess_number] #převede hodnoty listu na int
            return number_list

    
      

def comparing(guess_number_list, random_number_list):

    """Oba listy čísel porovná a přidává hodnoty do bulls and cows"""

    bulls = 0
    cows = 0
    for i in range(4):
        if guess_number_list[i] == random_number_list[i]:
            bulls += 1
        elif guess_number_list[i] in random_number_list:
            cows += 1
    
    return bulls, cows


def play_again():

    """po správném uhodnutí zeptá uživatele, zda chce pokračovat"""

    while True:
        choice = input("Do you want to play again? (Yes/No): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    
      
def game():

    """Spouští samotnou hru, definovány nové proměnné - pokusy, časomíra """

    while True:
        attempts = 0 #pokusy
        program_number = generate_number()
        starting_time = time.time() #časomíra

        while True:
            attempts += 1
            user_number = get_guess()
            bulls, cows = comparing(user_number, program_number)

            print(f"Bulls: {bulls}, Cows: {cows}, Attempts: {attempts}")

            if bulls == 4:
                end_time = time.time() 
                elapsed_time = round(end_time - starting_time, 2) #vyhodnocení uplynulého času
                print(f"Congrats, you've completed this game in {attempts} attempts and under {elapsed_time} seconds!")
                if attempts < 4:
                    print("You're a wizzard!")
                elif 4 <= attempts < 10:
                    print("You're on fire!")
                elif 10 <= attempts < 15:
                    print("Great job!")
                elif 15 <= attempts < 20:
                    print("Good Game!")
                elif attempts >= 20:
                    print("Try to complete the game in fewer attempts next time")
                
                if play_again():
                    break  
                else:
                    quit()  # Program se ukončí
            
            
                  
if __name__ == "__main__": #program se spustí pouze přímo, ne přes import jako modul
    game()


