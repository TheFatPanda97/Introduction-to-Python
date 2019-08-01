import random
print('welcome to the fortune teller')
print('all of these are true')
print('good luck my friend now letsss start..............')

def fortune():
        ask = True
        while ask == True:
           a1ilen = input("Ask a yes or no question [Say 'end game' to end game]:")

           if a1ilen == "end game" or a1ilen == "End Game":
                ask = False
                print('Endingggggg...................')
                print('Done!')

           else:
                answer = ['yes', 'no', 'probably', 'probably not', 'nopeee', 'most likely','yessssssssss','noooooooooooo',
                'most likely not', '100% yes']
                print(random.choice(answer))
print(fortune())

def commands(x):
        if x == 'shawn' == 'lolidod':
            a2a = input('admin enabled, type in a command:')
        if a2a == 'end':
            ask = False
            print('ending game...')
            print("done")
        elif a2a == 'rig':
            ask = "Rig"
        elif a2a == 'chosen outcome':
            ask = 'chose'
class fortunes:
    def __init__(self,ya,noo,maybe):
        self.ya = ya
        self.noo = noo
        self.maybe = maybe
        self.numbers = random
        return self.random(0,self)


