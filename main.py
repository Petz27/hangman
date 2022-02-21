import time

import gallows as g
import re
import os

def print_list(l):
    s = ""
    for element in l:
        s += element
    print(s)

def start_game(word):
    solution = word.upper()
    gallows = g.gallows
    first_letter_appearance = solution.count(solution[0])
    whitespaces = solution.count(" ")
    fin = len(solution)-first_letter_appearance-whitespaces

    correct = 0
    max_errors = 6
    errors = 0
    wrong_letters = []
    solved = []
    tried_letters = []
    tried_letters.append(solution[0])
    gameover = False

    for x in range(0, len(solution)):
        if solution[x] == " ":
            solved.append(" ")
        elif solution[x] == solution[0]:
            solved.append(solution[x])
        else:
            solved.append("_")
    while correct < fin:
        if errors > 0:
            print(gallows[errors])
        if wrong_letters:
            print("Wrong Letters: ", wrong_letters)
        if errors == max_errors:
            os.system('cls')
            print("GAME OVER")
            print("Solution: ", solution)
            print("Euer Versagen benötigt ein Opfer!")
            gameover = True
            break
        print_list(solved)
        letter = input("next letter: ").upper()
        if letter in tried_letters:
            os.system('cls')
            print("Try another letter!")
        elif letter in solution:
            tried_letters.append(letter)
            print(letter, " was correct!")
            count = solution.count(letter)
            correct += count
            indices = [i.start() for i in re.finditer(letter, solution)]
            for x in range(0, count):
                solved[indices[x]] = letter
            os.system('cls')
            print(f"correct: {correct}/{fin}")
        else:
            errors += 1
            wrong_letters.append(letter)
            tried_letters.append(letter)
            os.system('cls')
            print(f"incorrect: {correct}/{fin}")

    if not gameover:
        print("YOU HAVE SOLVED THE PUZZLE!")
        print(solution)

os.system("cls")
start_game(g.sol)
print("Thanks for playing!")
