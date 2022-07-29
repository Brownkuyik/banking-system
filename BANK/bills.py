import random
import string
import time
import pyinputplus as ent

def Bill(self):
        passcode = int(input('Code:'))
        cad = int(input('Enter account number:\n'))
        while True:
            if passcode==self.pin and cad == self.account_number:
              print(self.info())       
              print('Select the bil to bw paid\n1. light\n2. decoder\n3. fun wallet\n4. remita')
              what = int(input('Enter what to do below\n>>>>>  '))
              if what ==1:
                  print(f'Welcome {self.name.upper()} to our electricity payment platform')
                  amt = int(input('Enter amount to be send below\n>>>>>'))
                  if amt<=self.__account_balance:
                        print(f'Dear {self.name.upper()}.\nYou have succesfully pay {amt} for you electricity bill')
                        money = self.__account_balance-amt
                        print(self.TextFile())
                        with open(self.name + ' Account Balance.txt', 'a') as ledgerFile:
                            ledgerFile.write('\n\n================== ELECTRICITYBILL PAYMENT RECEIPT ====================\n')
                            ledgerFile.write(f'Name:                  \t {self.name} \n')
                            ledgerFile.write(f'Account Number:        \t {self.account_number} \n')
                            ledgerFile.write(f'Amount Payed:         \t {amt}\n')
                            ledgerFile.write(f'Amount remain:         \t {money}\n')
                            ledgerFile.write(f'Transaction date:     \t {time.asctime()} \n\n')
                            ledgerFile.write(f'\tpayment for your electricity bill\t\n')
                            ledgerFile.write(f'\n\n==============THANKS FOR BANKING WITH US==================\n\n')
                        break
                            
                  else:
                      print('insuficient fun')
                      break
              elif what ==2:
                  print('Welcome to our television subscription channel.\nPLs select 1.Gotv\n2. DSTV\n3. others')
                  ent =int(input('>>>>>>>>   '))
                  if ent == 1:
                      print('Press\n1. For one month\n2 for two months\n3. others.')
                      mont =int(input('>>>>>>>   '))
                      amount = mont * 1200
                      with open(self.name + ' Account Balance.txt', 'a') as ledgerFile:
                            ledgerFile.write('\n\n================== BILL PAYMENT RECEIPT ====================\n')
                            ledgerFile.write(f'Name:                  \t {self.name.upper()} \n')
                            ledgerFile.write(f'Account Number:        \t {self.account_number} \n\n')
                            ledgerFile.write(f'Number of months to be subscribed: \t{mont}\n\n')
                            ledgerFile.write(f'Amount it cost:         \t{amount}\n\n')
                            ledgerFile.write(f'Transaction date:\t {time.asctime()} \n')
                            ledgerFile.write(f'\t\tpayment for your electricity bill\t\n')
                            break
                  elif ent == 2:
                       print('Welcome to our DSTV channel.\nPress\n1. For one month\n2 for two months\n3. others.')
                       mont =int(input('>>>>>>>   '))
                       aount = mont * 2000
                       with open(self.name + ' Account Balance.txt', 'w') as ledgerFile:
                            ledgerFile.write('\n\n================== BILL PAYMENT RECEIPT ====================\n')
                            ledgerFile.write(f'Name:                  \t {self.name.upper()} \n')
                            ledgerFile.write(f'Account Number:        \t {self.account_number} \n\n')
                            ledgerFile.write(f'Number of months to be subscribed: \t{mont}\n\n')
                            ledgerFile.write(f'Amount it cost:         \t{aount}naira\n\n')
                            ledgerFile.write(f'Transaction date:\t {time.asctime()} \n')
                            ledgerFile.write(f'\t\tpayment for your electricity bill\t\n')
                            break
                  elif ent ==3:
                      print('the options are loading to be shown very soon.\nPls contact our customer care for the other side.')
                  else:
                      print(self.InvalidInfo())