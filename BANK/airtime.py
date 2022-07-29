
import time
import pyinputplus as ent
from validation import *

def Airtime(self):
        contact = int(input('Enter the destination phone number:    '))
        if contact >= 12 and contact <= 10:
            print('incomplete number')
        else:
            pass
        self.contact = contact
        amount = int(input('How much you want:\t'))
        self.amount =amount
        if (self.amount >= self.account_balance):
            print('Insufficent ammount')
        elif self.amount <= 50:
            print('invalid entry')
        else:
            pass
        

        pincode = int(input('Enter pin >>>> '))
        acccount_number = int(input('Account number >>'))
        card = int(input('enter card details >>> '))

        while True:
            if  card ==self.card_number and pincode ==self.pin and acccount_number==self.account_number:
                print(self.info())

                if (self.amount < self.__account_balance) and (self.amount >= 50):
                    print(f"You have sended a reacharge card of {self.amount} to {self.contact}")
                    self.__account_balance -=self.amount
                else:
                    print('amount not recommended')

                print(self.TextFile())
                with open(self.name.upper() +'Account balance.txt' 'a') as ledgerFile:
                    ledgerFile.write('\n\n=============Recharger recept===========')
                    ledgerFile.write(f'\nPhone number:\t {self.contact}\n')
                    ledgerFile.write(f'Amount Recharge:\t{self.amount}')
                    ledgerFile.write(f'Transaction date:\t {time.asctime()} \n')
                    break
            else:
                print(self.InvalidInfo())
                break