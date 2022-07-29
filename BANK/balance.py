import random
import string
import time
import pyinputplus as ent
from validation import *

class Acc:
    def CheckBalanace(self):
        pincode = int(input('Enter pin >>>> '))
        acccount_number = int(input('Account number >>'))
        card = int(input('enter card details >>> '))
        while True:
            if  card ==self.card_number and pincode ==self.pin and acccount_number==self.account_number:
                print(self.info()) #checking the customer info before proceding into the main work
                with open(self.name + 'Account balance.txt', 'w') as ledgerFile:
                    ledgerFile.write('==========ACCOUNT STATEMENT==========')
                    ledgerFile.write(f'\nAccount Name:\t\t {self.name.upper()} \n')
                    ledgerFile.write(f'Account Number:\t\t {self.account_number} \n')
                    ledgerFile.write(f'Account Balance:\t {self.__account_balance} Naira \n')
                    ledgerFile.write(f'Transaction date:\t {time.asctime()} \n')
                    ledgerFile.write('Thank you for banking with us'.center(100, '+'))
                    break  
            else:
                print(self.InvalidInfo())
                break
