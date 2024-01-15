import time
import random
from tqdm import tqdm


def nxt(val):
    a = []
    while val % 4 != 0:
        a.append(val + 1)
        val += 1
    return a


def comp(val):
    if val == 20:
        ran = 1
    elif val == 19:
        ran = random.randint(1, 2)
    else:
        ran = random.randint(1, 3)
    if ran == 1:
        print(val + 1)
        val += 1
    elif ran == 2:
        print(val + 1, val + 2)
        val += 2
    elif ran == 3:
        print(val + 1, val + 2, val + 3)
        val += 3
    return val


def choose(s, s2, val):
    print(s, "turn")
    print("Enter 1 :For input", val + 1, val + 2, val + 3)
    print("Enter 2 :For input", val + 1, val + 2)
    print("Enter 3: For input", val + 1)
    choice = input("Enter your choice : ")
    while choice != '1' and choice != '2' and choice != '3':
        print("Wrong input")
        choice = input("RE-enter your choice : ")
    if choice == '1':
        print(s2, "entered")
        print(val + 1, val + 2, val + 3)
        val += 3
    elif choice == '2':
        print(s2, "entered")
        print(val + 1, val + 2)
        val += 2
    elif choice == '3':
        print(s2, "entered")
        print(val + 1)
        val += 1
    return val


def choose19(s, s2, val):
    print(s, "turn")
    print("Enter 1 :For input", entry + 1, entry + 2)
    print("Enter 2: For input", entry + 1)
    choice = input("Enter your choice : ")
    while choice != '1' and choice != '2':
        print("Wrong input")
        choice = input("RE-enter your choice : ")
    if choice == '1':
        print(s2, "entered")
        print(val + 1, val + 2)
        val += 2
    elif choice == '2':
        print(s2, "entered")
        print(val + 1, val + 1)
        val += 1
    return val


def choose20(s, s2, val):
    print(s, "turn")
    print("Enter 1: For input", val + 1)
    choice = input("Enter your choice : ")
    while choice != '1':
        print("Wrong input")
        choice = input("RE-enter your choice : ")
    if choice == '1':
        print(s2, "entered")
        print(val + 1)
        val += 1
    return val


print("Hello!!!!")
time.sleep(1)
print("Welcome to the Game of 21")
time.sleep(2)
for i in tqdm(range(10)):
    time.sleep(.2)
instr = input("Enter 1 for instruction \nEnter 0 to continue\n")
while instr != '1' and instr != '0':
    print("Wrong input")
    instr = input("Re-enter your choice : ")
if instr == "1":
    print("Rules for the game")
    print("------------------------------------------------------------------------------------")
    print("1: Player 1 gets to enter a maximum of three consecutive digits starting with 1")
    print("2: Player 2 shall enter a maximum of three consecutive digits starting with last entered digit ")
    print("3: This shall continue turn by turn until a player ends on 21 ")
    print("4: Player who ends on 21 loses the game")
    time.sleep(7)
restart = '0'
while True:
    print("Choose Game Mode")
    print("1 for Easy Mode(Vs computer)")
    print("2 for Difficult Mode(Vs computer)")
    print("3 for 1 vs 1 Mode(2 player)")
    n = input("Enter your choice: ")
    time.sleep(1)
    while n != '1' and n != '2' and n != '3':
        print("Wrong input")
        n = input("Re-enter your choice : ")
    entry = 0
    if n == '1':
        print("Entering EASY MODE")
        print("choose the turn")
        print("1 or 2")
        z = input()
        num = 1
        while z != '1' and z != '2':
            print("Wrong input")
            z = input("Enter your choice : ")
        if z == '2':
            print("It's computers turn")
            print("Computer entered 1")
            entry += 1
            time.sleep(1)
        while True:
            if entry == 19:
                entry = choose19("Your", "You", entry)
            elif entry == 20:
                entry = choose20("Your", "You", entry)
            else:
                entry = choose("Your", "You", entry)
            if entry == 21:
                print("You lost")
                print("BETTER LUCK NEXT TIME")
                restart = input("Do you want to play again ?\nEnter 1 of restart \nEnter 0 to exit\n")
                break
            time.sleep(1)
            print("It's computers turn")
            print("computer entered")
            entry = comp(entry)
            if entry >= 21:
                print("You Won")
                restart = input("Do you want to play again ?\nEnter 1 of restart \nEnter 0 to exit\n")
                break
            time.sleep(1)
    elif n == '2':
        print("Entering DIFFICULT MODE")
        print("Choose the turn")
        print("1 or 2")
        time.sleep(1)
        z = input()
        while z != '1' and z != '2':
            print("Wrong input")
            z = input("Enter your choice : ")
        if z == '2':
            print("It's computers turn")
            print("Computer entered")
            print("1")
            time.sleep(1)
            entry += 1
        while True:
            if entry == 19:
                entry = choose19("Your", "You", entry)
            elif entry == 20:
                entry = choose20("Your", "You", entry)
            else:
                entry = choose("Your", "You", entry)
            if entry == 21:
                print("You lost")
                print("BETTER LUCK NEXT TIME")
                restart = input("Do you want to play again?\nEnter 1 of restart \nEnter 0 to exit\n")
                break
            time.sleep(1)
            print("It's computers turn")
            if entry % 4 == 0:
                print(entry+1)
                entry += 1
            else:
                print("Computer entered")
                m = nxt(entry)
                entry = m[-1]
                print(*m)
            if entry == 21:
                print("You Won")
                restart = input("Do you want to play again ?\nEnter 1 of restart \nEnter 0 to exit\n")
                break
            time.sleep(1)
    elif n == '3':
        print("Entering 1 vs 1 mode ")
        time.sleep(1)
        while True:
            if entry == 19:
                entry = choose19("Player 1", "Player 1", entry)
            if entry == 20:
                entry = choose20("Player 1", "Player 1", entry)
            else:
                entry = choose("Player 1", "Player 1", entry)
            if entry >= 21:
                print("Player 2 won")
                print("Player 1 BETTER LUCK NEXT TIME")
                restart = input("Do you want to play again ?\nEnter 1 of restart \nEnter 0 to exit\n")
                break
            time.sleep(1)
            if entry == 19:
                entry = choose19("Player 2", "Player 2", entry)
            elif entry == 20:
                entry = choose20("Player 2", "Player 2", entry)
            else:
                entry = choose("Player 2", "Player 2", entry)
            if entry >= 21:
                print("Player 1 won")
                print("Player 2 BETTER LUCK NEXT TIME")
                restart = input("Do you want to play again ?\nEnter 1 of restart \nEnter 0 to exit\n")
                break
            time.sleep(1)
    if restart == '0':
        exit()
