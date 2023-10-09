import os
import msvcrt
import random
import time

def draw_border(x=0, y=0, width=30, height=3):
    v = chr(186)  # vertical
    h = chr(205)  # horizontal
    tr = chr(187)  # top right border
    br = chr(188)  # bottom right border
    tl = chr(201)  # top left border
    bl = chr(200)  # bottom left border
    
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            print("\033[%d;%dH" % (i + y, j + x), end="")
            if i == 1 and j == 1:
                print(tl, end="")
            elif i == height and j == 1:
                print(bl, end="")
            elif i == 1 and j == width:
                print(tr, end="")
            elif i == height and j == width:
                print(br, end="")
            elif i == 1 or i == height:
                print(h, end="")
            elif j == 1 or j == width:
                print(v, end="")
    print()

def check_password_strength(password):
    excess = max(0, len(password) - 6)
    base_score = 50
    num_upper = sum(c.isupper() for c in password)
    num_lower = sum(c.islower() for c in password)
    num_digit = sum(c.isdigit() for c in password)
    num_symbol = len(password) - num_upper - num_lower - num_digit
    
    bonus_excess = 3
    bonus_upper = 4
    bonus_numbers = 5
    bonus_symbols = 5
    bonus_combo = 0
    
    if num_upper > 0 and num_digit > 0 and num_symbol > 0:
        bonus_combo = 25
    elif (num_upper > 0 and num_digit > 0) or (num_upper > 0 and num_symbol > 0) or (num_digit > 0 and num_symbol > 0):
        bonus_combo = 15
    
    score = base_score + (excess * bonus_excess) + (num_upper * bonus_upper) + (num_digit * bonus_numbers) + (num_symbol * bonus_symbols) + bonus_combo
    
    return score

while True:
    os.system("cls")
    print("±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±")
    print("\t\t  ±±±±± ")
    print("\t\t  ±   ± ")
    print("\t\t±±±±±±±±±")
    print("\t\t±±±± ±±±±")
    print("\t\t±±±±±±±±±")
    print()
    print("        PASSWORD  STRENGTH  CHECKER      ")
    print("±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±")
    print()
    
    password = input("\tEnter Password: ")
    
    score = check_password_strength(password)
    
    print("\nChecking Password Strength...", end="")
    time.sleep(0.5)
    print("\n\n", end="")
    
    draw_border(7, 10)
    
    print("\033[11;9HPassword Status: ", end="")
    if score < 50:
        print("Weak")
    elif score >= 50 and score < 75:
        print("Average")
    elif score >= 75 and score < 100:
        print("Strong")
    elif score >= 100:
        print("Secure")
    
    print("\033[15;9HDo you want to generate password again (y/n): ", end="")
    op = msvcrt.getch().decode('utf-8').lower()
    if op != 'y':
        break
