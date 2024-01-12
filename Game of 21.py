import time
import random
from tqdm import tqdm
def nxt(n):
    a = []
    while n % 4 != 0:
        a.append(n + 1)
        n += 1
    return a

def choose(s, s2, entry):
    print(s, "turn")
    print("Enter 1 :For input", entry + 1, entry + 2, entry + 3)
    print("Enter 2 :For input", entry + 1, entry + 2)
    print("Enter 3: For input", entry + 1)
    choice = input("Enter your choice : ")
    while choice != '1' and choice != '2' and choice != '3':
        print("Wrong input")
        choice = input("RE-enter your choice : ")
    if choice == '1':
        print(s2, "entered")
        print(entry + 1, entry + 2, entry + 3)
        entry += 3
    elif choice == '2':
        print(s2, "entered")
        print(entry + 1, entry + 2)
        entry += 2
    elif choice == '3':
        print(s2, "entered")
        print(entry + 1)
        entry += 1
    return entry
print("Hello!!!!")
time.sleep(1)
print("Welcome to the Game of 21")
time.sleep(2)
for i in tqdm(range(10)):
    time.sleep(.25)
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
while True:
    print("Choose Game Mode")
    print("1 for Easy Mode")
    print("2 for Difficult Mode")
    print("3 for 1 vs 1 Mode")
    time.sleep(2)
    n = input("Enter your choice: ")
    time.sleep(1)
    while n != '1' and n != '2' and n != '3':
        print("Wrong input")
        n = input("Re-enter your choice : ")
    entry = 0
    if n == '2':
        print("Choose the turn")
        print("1 or 2")
        time.sleep(2)
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
            entry = choose("Your", "You", entry)
            if entry >= 21:
                print("You lost")
                restart = input("Do you want to play again \n Enter 1 of restart \n Enter 0 to exit\n")
                break
            time.sleep(3)
            print("It's computers turn")
            if entry % 4 == 0:
                print(entry+1)
                entry += 1
            else:
                print("Computer entered")
                m = nxt(entry)
                entry = m[-1]
                print(*m)
            if entry >= 21:
                print("You Won")
                restart = input("Do you want to play again \n Enter 1 of restart \n Enter 0 to exit\n")
                break
            time.sleep(3)
    elif n == '1':
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
            time.sleep(2)
        while True:
            entry = choose("Your", "You", entry)
            if entry >= 21:
                print("You lost")
                restart = input("Do you want to play again \n Enter 1 of restart \n Enter 0 to exit\n")
                break
            time.sleep(2)
            ran = random.randint(1, 3)
            print("It's computers turn")
            print("computer entered")
            if ran == 1:
                print(entry+1)
                entry += 1
            elif ran == 2:
                print(entry+1, entry+2)
                entry += 2
            elif ran == 3:
                print(entry+1, entry+2, entry+3)
                entry += 3
            if entry >= 21:
                print("You Won")
                restart = input("Do you want to play again \n Enter 1 of restart \n Enter 0 to exit\n")
                break
            time.sleep(2)
    elif n == '3':
        print("Entering 1 vs 1 mode ")
        time.sleep(1)
        while True:
            entry = choose("Player 1", "Player 1", entry)
            if entry >= 21:
                print("Player 2 won")
                print("Player 1 BETTER LUCK NEXT TIME")
                restart = input("Do you want to play again \n Enter 1 of restart \n Enter 0 to exit\n")
                break
            time.sleep(1)
            entry = choose("Player 2", "Player 2", entry)
            if entry >= 21:
                print("Player 1 won")
                print("Player 2 BETTER LUCK NEXT TIME")
                restart = input("Do you want to play again \n Enter 1 of restart \n Enter 0 to exit\n")
                break
            time.sleep(1)
    if restart == '0':
        exit()
