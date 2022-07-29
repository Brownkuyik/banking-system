import time
def info(self):
        time.sleep(2)
        print(f'Dear {self.name.upper()},\nAuthenticating your pin')
        
        time.sleep(5)
        print(f'Checking your card number and your ccv')
        print('loading.....................')
        

        time.sleep(2)
        print(f'access approve'.center(500))

        time.sleep(7)
        print(f'Your information of account number {self.account_number} is succesfully validated into our bank')
        print('thank you for choosing us as your prefered bank')
        return('your details is secured and save')




'''From this section down is only for an invalid errors that may arise due to the course of customer mistakses.'''


def InvalidInfo(self):
        print('loading..................'.rjust(300))
        time.sleep(5)
        return('Your details are incorrect check again and try after 10 minutes\nThanks for your understanding.')

def incom(self):
    return('you just enter am incomplete account number')

def pass_error(self):
    return('Pls enter a complet four digit password of your account')


def Wrong():
        return('Dear customer please enter a valid details')
