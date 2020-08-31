"""
1. Give a prompt to user asking if they wish to create a new Savings account or access an existing one
2. If user would like to create a new account,accept their name and initial deposit, and
create a 5 digit "random number" and make it as the account number of their new savings account
3. If they are accessing an existing account, accept their name and account number to validate the user and give them options
to withdraw, deposit or display their available balance
"""

#Import abstract method and random function

from abc import ABCMeta,abstractmethod
from random import randint

class Account(metaclass = ABCMeta):

    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0


class SavingAccount(Account):
    def __init__(self):
        self.SavingAccount = {}

    def createAccount(self,name,initialdeposit):
        print()
        self.accountNumber = randint(10000,99999)
        self.SavingAccount[self.accountNumber] = [name,initialdeposit]
        print("Congradulations! Your account has been created ")
        print("Your account number is: ",self.accountNumber)
        print()

    def authenticate(self,name,accountNumber):
        print()
        if accountNumber in self.SavingAccount.keys():
            if self.SavingAccount[accountNumber][0] == name:
                print("Authentication Successful!")
                self.accountNumber = accountNumber
                print()
                return True

            else:
                print("Authentication Failed")
                print()
                return False

        else:
            print("Authentication Failed")
            print()
            return False


    def withdraw(self,withdrawAmount):
        print("Enter withdraw amount")
        if self.SavingAccount[self.accountNumber][1] < withdrawAmount:
            print("Insufficient Balance!")
            print()

        else:
            self.SavingAccount[self.accountNumber][1] -= withdrawAmount
            print()
            print("Withdraw Successful!")
            print()
            self.displayBalance()

    def deposit(self,depositAmount):
        print()
        self.SavingAccount[self.accountNumber][1] += depositAmount
        print("Deposit Successful!")
        self.displayBalance()

    def displayBalance(self):
        print()
        print("Account Balance: ",self.SavingAccount[self.accountNumber][1])


# Create an object for account holder
savingsaccount = SavingAccount()
while True:
	print()
	print("Hi There! Welcome to our Banking system!")
	print()
	print("Please select an option below: ")
	print("Enter 1 for new savings account")
	print("Enter 2 for existing account")
	print("Enter 3 to quit")

	#ask for user choice
	userchoice = int(input())

	#check for options
	if userchoice == 1:
	    print("We would like you enter following details for new account")
	    print("Enter your name")
	    name = str(input())
	    print("Enter initial deposit for your account")
	    deposit = int(input())
	    savingsaccount.createAccount(name,deposit)
	    print()

	elif userchoice == 2:
	    print("Enter your name")
	    name = str(input())
	    print("Enter your account number")
	    account_number = int(input())
	    authenticatestatus= savingsaccount.authenticate(name,account_number)
	    print()
	    if authenticatestatus is True:
	        while True:
	                        print("Enter 1 for Withdraw")
	                        print("Enter 2 to Deposit")
	                        print("Enter 3 to display balance")
	                        print("Enter 4 to return to previous menu")
	                        userchoice_ = int(input())
	                        if userchoice_ == 1:
	                                print("Enter amount to withdraw")
	                                amount = int(input())
	                                savingsaccount.withdraw(amount)

	                        elif userchoice_ == 2:
	                                print("Enter amount to deposit")
	                                deposit_amount = int(input())
	                                savingsaccount.deposit(deposit_amount)

	                        elif userchoice_ == 3:
	                                print()
	                                savingsaccount.displayBalance()

	                        else:
	                                print("Returning to previous options")
	                                break

	else:
	    quit()


	        

