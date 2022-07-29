# thou copyed, the programm is to run an atm matchine functions

import random
import string
import time
import pyinputplus as ent
import balance 
import tranfar, airtime, bills




class AtmWork():
    def __init__(self, pin, name, cvv, number, cnumber): #To get customer details
        self.pin = pin
        self.name = name
        self.three_number= cvv
        self.card_number = number
        self.account_number = cnumber
        self.__account_balance = 10000000 #hide the amount the customer has in his acoount untill he used hid hand to request for it.
        
    
    
    def details(self ):
        self.account_number 
        self.pin 

    def TextFile(self):
        with open(self.name.upper() + 'Account Balance.txt', 'w' ) as ledgerFile:
            ledgerFile.write('STATEMENT OF YOUR ACCOUNT'.center(80, '='))
            ledgerFile.write(f'''account Name:\t{self.name.upper()}\n'''.ljust(40))
            ledgerFile.write(f'''account Number:\t{self.account_number}\n'''.ljust(40))
            # ledgerFile.write(f'''debit:  \t{self.amount}\n''')
            ledgerFile.write(f'''account balance:  \t{self.__account_balance}\n'''.ljust(40))
            ledgerFile.write(f'''transaction info.:  \t{time.asctime}\n'''.ljust(40))
            ledgerFile.write(f'''THANKS FOR BANKING WITH US'''.center(80, '='))

    def TRANSFAR(self):
        print(tranfar.Tranfer(self))

    def Pay_Bills(self):
        print(bills.Bill(self))

    def Buy_Airttime(self):
        print(airtime.Airtime(self))

    
    def Check_Balance(self):
        print(balance.Acc.CheckBalanace('self'))


        

    
    def Create_account():
        print('we discover that you dont have an account with us, so for that we decided ti get you you account.')
        fname = ent.inputName(prompt='Enter your first name\n')
        lname = ent.inputName(prompt='Enter your last name\n')
        mname = ent.inputName(prompt='Enter your middile name\n')
        phone = ent.inputNum(prompt='Enter your phone number \n')
        fname = ent.inputEmail(prompt='Enter your email')
        ente = 11
        cn = 3
        digitd = string.digits
        card_number = [random.choice(digitd) for i in range(cn)]
        my_account_number =[random.choice(digitd) for i in range(ente)]
        password =ent.inputPassword(prompt='enter your pincode here\n')
        account_name = fname.upper();lname.upper()
        '''
        
        i have a lot to do in this code which can take days based on how it is being handeled and also 
        i need help on how to look for information
        
        '''    

     

    # def CeckBalance(self):
        # print(balance.CheckBalanace())
    # print(Airtime())
    # print(Tranfer())
    # def Bill_payment(self):
    #     print(bills.Bill())

mine = AtmWork(1234,'kuyik brown',123,21,213)
emediong = AtmWork(3333, 'Emediong Mfon Etim', 1234,4321,2222)
idiot = AtmWork(4321,'akwamfon vincent dickson',908,5656,343434)
joe = AtmWork(234, 'JOSEPHIN STEKIM', 567,1122,112233)
        
# print(mine.TextFile())
# print(mine.CheckBalanace())
# print(idiot.CeckBalance())
# print(mine.Bill_payment())
print(joe.TRANSFAR())
# print(emediong.Check_Balance())