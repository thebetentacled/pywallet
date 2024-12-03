# budget tracker by thebetentacled
# This program is licensed under the terms of the GNU GPLv3 License.

# imports
import csv

# variables
walletcash = float(0.00)
coins = float(0.00)
savings = float(0.00)
checking = float(0.00)

# functions
def reset():
    global walletcash, coins, savings, checking
    walletcash = float(input("How much money is in your wallet? (bills only!) \n  --> "))
    coins = float(input("How much money do you have in coins? \n  --> "))
    savings = float(input("How much money is in your savings? \n  --> "))
    checking = float(input("How much money is in your checking account? \n  --> "))

def subtract():
    global walletcash, coins, savings, checking
    amount = float(input("Subtract how much? \n --> "))
    print("Subtract from what? (enter only the number)")
    print("  1) Wallet")
    print("  2) Coins")
    print("  3) Savings")
    print("  4) Checking")
    fromwhat = int(input("  --> "))
    if fromwhat == 1:
        walletcash = walletcash - amount
    elif fromwhat == 2:
        coins = coins - amount
    elif fromwhat == 3:
        savings = savings - amount
    elif fromwhat == 4:
        checking = checking - amount
    else:
        subtract()

def add():
    global walletcash, coins, savings, checking
    amount = float(input("Add how much? \n --> "))
    print("Add to what? (enter only the number)")
    print("  1) Wallet")
    print("  2) Coins")
    print("  3) Savings")
    print("  4) Checking")
    fromwhat = int(input("  --> "))
    if fromwhat == 1:
        walletcash = walletcash + amount
    elif fromwhat == 2:
        coins = coins + amount
    elif fromwhat == 3:
        savings = savings + amount
    elif fromwhat == 4:
        checking = checking + amount
    else:
        add()

def setamount():
    global walletcash, coins, savings, checking
    amount = float(input("Set balance to what amount? \n --> "))
    print("Set what? (enter only the number)")
    print("  1) Wallet")
    print("  2) Coins")
    print("  3) Savings")
    print("  4) Checking")
    fromwhat = int(input("  --> "))
    if fromwhat == 1:
        walletcash = amount
    elif fromwhat == 2:
        coins = amount
    elif fromwhat == 3:
        savings = amount
    elif fromwhat == 4:
        checking = amount
    else:
        setamount()

def save():
    global walletcash, coins, savings, checking
    # organize data
    fields = ["location", "amount"]
    rows = [
        ["wallet", str(walletcash)],
        ["coins", str(coins)],
        ["savings", str(savings)],
        ["checking", str(checking)],
    ]
    # write to data.csv
    data = open("data.csv", "w")
    writer = csv.writer(data)
    writer.writerow(fields)
    writer.writerows(rows)


def load():
    global walletcash, coins, savings, checking
    # get data
    fields = []
    rows = [[], [], [], []]
    data = open("data.csv", "r")
    reader = csv.reader(data)
    fields = next(reader)
    for row in reader:
        rows.append(row)
    walletcash = rows[1][2]
    coins = rows[2][2]
    savings = rows[3][2]
    checking = rows[4][2]

def loop():
    print("What would you like to do?")
    print("  1) Reset")
    print("  2) Subtract")
    print("  3) Add")
    print("  4) Set Amount ")
    print("  5) Save")
    print("  6) Load")
    choice = int(input("  --> "))
    if choice == 1:
        reset()
        loop()
    elif choice == 2:
        subtract()
        loop()
    elif choice == 3:
        add()
        loop()
    elif choice == 4:
        setamount()
        loop()
    elif choice == 5:
        save()
        loop()
    elif choice == 6:
        load()
        loop()
    else:
        loop()

# main
print("Welcome to walletpy!")
print("This is a free budget tracker made by thebetentacled (check out my github)")
print("This program is licensed under the terms of the GNU GPLv3 License.")
loop()
