# Jonathan Veltri
# CS 175
# Assignment 6

balance = 0
isCard = False
end = False
flag = "f"
Type = ""

def menu():
    print("\nATM\n")
    print("Option 1: Deposit")
    print("Option 2: Withdraw")
    print("Option 3: Check Balance")
    print("Option 4: Print Transactions")
    print("Option 5: Exit")
    choice = int(input("Select an option: "))
    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        print(f"\nYour balance is ${balance:.2f}")
    elif choice == 4:
        print_transaction(flag)
    elif choice == 5:
        print("Goodbye!")
        global end
        end = True
    else:
        print("The choice is invalid!")

def validate_card_number(cardNum):
    return 1000 <= cardNum <= 9999

def validate_card_password(password):
    count = 3
    while count > 0:
        input_password = input("What is your password?: ")
        if input_password == password:
            return True
        count -= 1
        if count != 0:
            print(f"You have {count} more times to type your password!")
    print("Your card is locked!")
    print("Goodbye!")
    exit()

def withdraw():
    global balance, flag
    amount = int(input("How much to withdraw?: $"))
    if amount < 0:
        print("The withdrawal amount is negative!")
    elif amount > balance:
        print("The amount is greater than the balance!")
    else:
        oldBalance = balance
        balance -= amount
        print(f"Withdrawal successful. Your new balance is ${balance:.2f}")
        Type = "Withdraw"
        flag = "t"
        save_transaction(Type, balance, oldBalance)

def deposit():
    global balance, oldBalance, flag
    amount = int(input("How much to deposit?: $"))
    if amount < 0:
        print("The deposit amount is negative!")
    else:
        oldBalance = balance
        balance += amount
        print(f"Deposit successful. Your new balance is ${balance:.2f}")
        Type = "Deposit"
        flag = "t"
        save_transaction(Type, balance, oldBalance)

def save_transaction(Type, balance, oldBalance):
    with open("BOA.txt", "a") as txt:
        txt.write(f"{Type:>16}{oldBalance:>11.2f}${(balance - oldBalance):>10.2f}${balance:>15.2f}$\n")


def print_transaction(flag):
    if flag == "f":
        print("\nThere are no transactions!")
    else:
        print("Transaction History\n")
        with open("BOA.txt", "r") as txt:
            for line in txt:
                print(line)
    menu()



def main():
    global isCard
    while not isCard:
        cardNum = int(input("What is your BOA card number (1000 - 9999)?: "))
        isCard = validate_card_number(cardNum)
        if not isCard:
            print("The Card number must be 1000 - 9999!")

    password = str(cardNum)[1:4]
    print("Welcome to Bank of America!")
    if not validate_card_password(password):
        print("Incorrect password. Your card is locked!")
        exit()
    with open("BOA.txt", "w") as txt:
        txt.write(f"     Transaction     Balance     Amount     New Balance\n")

    while not end:
        menu()

main()