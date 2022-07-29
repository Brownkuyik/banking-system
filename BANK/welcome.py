from main import AtmWork
from validation import *


address = 'WELCOME TO BEZEMER BANK'.center(80)
inst = 'we are working very hard to make sure that you are dully attended to as at when due.'.capitalize()
entry = 'what do u what to do?'.upper()
b = ['TRANFAR', 'AIRTIME', 'CHECK BALANCE', 'BILLS']

class WELCOME:
    while True:

        def Done():
            print(address,'\n',inst, '\n\n\n\n',entry)
            for number, demand in enumerate(b, start=1):
                print(f"{number}\t{'='} \t{demand}\n")
            return
        try:
            enter = int(input('\nEnter what you want below\n>>>\t'.upper()))
            if enter == 1:
                print('\n\n')
                print(AtmWork.TRANSFAR('self'))

        except ValueError:
            print(Wrong())
            




























        Done()

