# Miguel Narciso
# Assignment 10.1: Your Own Class
# Acknowledgements

from random import random

# Creates an ATM object
class ATM:
    def __init__(self, amount, change):
        self._amount = amount
        self._change = change
    
    def get_amount(self):
        return self._amount
    
    def set_amount(self, amount):
        self._amount = amount

    def get_change(self):       
        return self._change
    
    def set_change(self, change):
        self._change = change

# Creates ATM with either random values or user-inputted values
def create_ATM():
    #new_atm = ATM(#Insert Amount Here, #Insert Change Here)
    new_atm = ATM((random() * 1000), random() * 100)
    
    return new_atm

# Formats into $X.XX
def money_format(num):
    money = (f'${abs(num):.2f}')
    return money

# Subtracts the selected value from the amount and change
def withdraw(new_atm, selection):
    # Checks if the ATM has enough money to withdraw the selcted value
    if (new_atm.get_change() > selection):
        change = new_atm.get_change() - selection
        new_atm.set_change(change)

        amount = new_atm.get_amount() - selection
        new_atm.set_amount(amount)
    else:
        print("\nI'm sorry, this ATM doesn't have enough cash. Please try again another time.")

# Adds the selected value to the amount and change
def deposit(new_atm, selection):
    amount = new_atm.get_amount() + selection
    new_atm.set_amount(amount)
    
    change = new_atm.get_amount() + selection
    new_atm.set_change(change)

def main():
    n = "\n"
    t = "\t"
    new_atm = create_ATM()

    # Loops until user is done
    while(True):
        print(f"Account Balance: {money_format(new_atm.get_amount())}")
        # Prompts the user to choose type of transaction
        user_input = input(f"{n}Select type of transaction"
                           f"{n}{t}0: Withdraw Amount"
                           f"{n}{t}1: Deposit Amount"
                           f"{n}{t}2: Done{n}"
                           f"{n}Selection: ")
        # User selected Withdraw
        if (user_input == "0"):
            # Prompts the user to choose how much money to withdraw
            user_input = input(f"{n}How much are you withdrawing"
                        f"{n}{t}0: $1"
                        f"{n}{t}1: $5"
                        f"{n}{t}2: $10"
                        f"{n}{t}3: $50"
                        f"{n}{t}4: $100"
                        f"{n}{t}5: Cancel{n}"
                        f"{n}Selection: ")
    
            if (user_input == "0"):
                withdraw(new_atm, 1)
            elif (user_input == "1"):
                withdraw(new_atm, 5)
            elif (user_input == "2"):
                withdraw(new_atm, 10)
            elif (user_input == "3"):
                withdraw(new_atm, 50)
            elif (user_input == "4"):
                withdraw(new_atm, 100)
            elif (user_input == "5"):
                break
            else:
                print("Invalid selection. Please make another selection.")
        
        # User selected deposit
        elif(user_input == "1"):
            # Loops until user is done
            while(True):
                # Asks the user if they're depositing dollar bills or coins
                user_input = input(f"{n}What are you depositing?"
                            f"{n}{t}0: Dollar"
                            f"{n}{t}1: Coin"
                            f"{n}{t}2: Done{n}"
                            f"{n}Selection: ")
                # User chose dollar
                if (user_input == "0"):
                    # Prompts the user to choose how much money to deposit
                    user_input = input(f"{n}How much are you depositing?"
                            f"{n}{t}0: $1"
                            f"{n}{t}1: $5"
                            f"{n}{t}2: $10"
                            f"{n}{t}3: $50"
                            f"{n}{t}4: $100"
                            f"{n}{t}5: Cancel{n}"
                            f"{n}Selection: ")
                    
                    if (user_input == "0"):
                        deposit(new_atm, 1)
                    elif (user_input == "1"):
                        deposit(new_atm, 5)
                    elif (user_input == "2"):
                        deposit(new_atm, 10)
                    elif (user_input == "3"):
                        deposit(new_atm, 50)
                    elif (user_input == "4"):
                        deposit(new_atm, 100)
                    elif (user_input == "5"):
                        break
                    else:
                        print("Invalid selection. Please make another selection.")
                
                # User chose coin
                elif (user_input == "1"):
                    # Prompts the user to choose how much money to deposit
                    user_input = input(f"{n}How much are you depositing?"
                            f"{n}{t}0: 1¢"
                            f"{n}{t}1: 5¢"
                            f"{n}{t}2: 10¢"
                            f"{n}{t}3: 25¢"
                            f"{n}{t}4: Cancel{n}"
                            f"{n}Selection: ")
                    
                    if (user_input == "0"):
                        deposit(new_atm, 0.01)
                    elif (user_input == "1"):
                        deposit(new_atm, 0.05)
                    elif (user_input == "2"):
                        deposit(new_atm, 0.10)
                    elif (user_input == "3"):
                        deposit(new_atm, 0.25)
                    elif (user_input == "4"):
                        break
                    else:
                        print("Invalid selection. Please make another selection.")

                elif (user_input == "2"):
                    break
                    
                else:
                    print("Invalid selection. Please make another selection.")
        # Prints a goodbye message and breaks the loop
        elif(user_input == "2"):
            print("Thank You. Come Again Soon.")
            done = True
            break
        
        # breaks the loop (used for debugging)
        elif(user_input == "break"):
            done = True
            break
        
        else:
            print("Invalid selection. Please make another selection.")

if __name__ == "__main__":
    main()