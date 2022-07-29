import time

from validation import *
welcome= f'dear esteem customer you are about to do a tranfar.\nConfirm the details before sending to avoid lost of fund'.capitalize()

def Tranfer(self):
    while True:
        try:
            
            print('fund tranfar'.upper().center(50, '='))
            print(welcome)
            print('\n')
            money = int(input('Amount to be send \n>>>>'))
            time.sleep(2)
            print('Enter recepian account details below\n')
            account = int(input('Account number >>>\t'))
            print('enter destination bank name:\t\n')
            bank = input('>>>\t')
            time.sleep(4)
            print('\nEnter your bank details below')
            passwor = int(input('\nEnter your pincode:\n>>>'))
            accoun = int(input('\nPls Enter your account number below:\n>>>'))
            
            time.sleep(2)
            transfar_code=int(input('Your tranfar code >>>>\t'))
            continue
        except:
            print('Wrong entry')
        

        while True:
            if passwor ==self.pin and accoun == self.account_number and transfar_code==self.card_number:
                print(info())
                
                if money < self.__account_balance:
                    print(f'congratulation {self.name.upper()}.\nYou have succesfully transfar{money} to {account}')
                    sent=self.__account_balance - money


                    print(self.TextFile())
                    with open(self.name +'account balance.txt', 'a') as ledgerFile:
                        ledgerFile.write('\n\nTRANSFER DETAILS\n\n'.center(40, '='))
                        ledgerFile.write(f'sender name:               \t{self.name}\n')
                        ledgerFile.write(f'Sender account number:       \t{accoun}\n')
                        ledgerFile.write(f'Reciever account number:            \t{account}\n')
                        ledgerFile.write(f'Bank name:                \t{bank}\n')
                        ledgerFile.write(f'Amount send:              \t{money}\n')
                        ledgerFile.write(f'account balance:        \t{sent}\n\n')
                        ledgerFile.write(f'Transaction date:\t {time.asctime()} \n\n')
                        ledgerFile.write(f'\n\n\t THANK YOU FOR BANKING WITH US.\t\n\n')
                else:
                    print('insuddicient fun for the tranfar')
                    break
            else:
                print(InvalidInfo())
                break
