import time


class Check_int:
    def __init__(self, equ):
        self.equ = equ

    def check_int(self):
        x = self.equ
        x.replace('+', '')
        x.replace('-', '')
        x.replace('*', '')
        x.replace('/', '')
        for i in x:
            if i != int():
                return 'that is not a number you idiot'
            else:
                q = 0


class setup:
    def setup():
        print('welcome')
        time.sleep(0.5)
        print('to')
        time.sleep(0.5)
        print('the awesome calculator')
        time.sleep(1)
        print('use me')
        time.sleep(0.5)
        print('as')
        time.sleep(0.5)
        print('you would')
        time.sleep(0.5)
        print('a small one')
        time.sleep(0.5)
        return 6


while 0 == 0:
    y = setup
    y.setup()
    x = input('what is your name')
    if x == 'shawn':
        time.sleep(0.5)
        print('we dont serve your type')
        break
    elif x == 'Shawn':
        time.sleep(0.5)
        print('we dont serve your type')
        break
    else:
        x = input(
            'okay ' + x + ' what would you like me to solve type end to end')
        while 0 == 0:
            if x == 'end':
                break
            elif x == 'End':
                break
            else:
                print(eval(x))
                time.sleep(0.2)
                x = input('next what do you want me to solve')
        break
