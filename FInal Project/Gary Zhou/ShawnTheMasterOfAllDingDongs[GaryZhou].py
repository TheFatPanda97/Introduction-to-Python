import time
import random
import pygame

guessed_letters = []
difficulty = {'shawn level': 8, 'easy': 7, 'medium': 6, 'hard': 5,
              'sean level': 4}


class idontknowhowtoname:
    def __init__(self, ll):
        self.ll = ll

    def Drawlines(self):
        if self.ll <= 5:
            pygame.draw.circle(screen, (0, 0, 0), (100, 100), 25, 1)
        if self.ll <= 4:
            pygame.draw.line(screen, (0, 0, 0), (100, 125), (100, 200))
        if self.ll <= 3:
            pygame.draw.line(screen, (0, 0, 0), (100, 200), (75, 225))
        if self.ll <= 2:
            pygame.draw.line(screen, (0, 0, 0), (100, 200), (125, 225))
        if self.ll <= 1:
            pygame.draw.line(screen, (0, 0, 0), (100, 150), (125, 133))
        if self.ll == 0:
            pygame.draw.line(screen, (0, 0, 0), (100, 150), (77, 125))


class word:
    def __init__(self, word):
        self.WO = word

    def __str__(self):
        return str(self.WO)

    def display_lines(self):
        display = ''
        for i in self.WO:
            if i in guessed_letters:
                display += (i + ' ')
            else:
                display += ('_ ')
        return display


def checkin(guess):
    if guess in guessed_letters:
        return 'Already'
    elif guess in str(chosenword):
        guessed_letters.append(guess)
        return True
    else:
        return False


def checkwin(guess, chosenword):
    a = 0
    for i in chosenword:
        if i in guessed_letters:
            a += 1
    if a == len(chosenword):
        return True
    elif guess == chosenword:
        return True


L1 = "This is the hangman creator"
L2 = "You will input words and then guess it"
L3 = "Or You can make a friend guess the word"
Start = [L1, L2, L3]

for i in Start:
    print(i)
    time.sleep(1)

words = (input('input the words you want, seperated by commas')).split(',')
chosenword = word(random.choice(words))
letters_left = (difficulty[input(
    'choose a difficulty: shawn level, easy, medium, hard or sean level')])
for i in range(0, 100):
    print('')
print('now it\'s time to guess')

while letters_left >= 0:
    a = 0
    left = idontknowhowtoname(letters_left)
    while a <= 3:
        if a == 3:
            break
        if a < 3:
            screen = pygame.display.set_mode((300, 300))
            screen.fill((255, 255, 255))
            pygame.draw.line(screen, (0, 0, 0), (175, 250), (250, 250))
            pygame.draw.line(screen, (0, 0, 0), (212.5, 250), (212.5, 50))
            pygame.draw.line(screen, (0, 0, 0), (212.5, 50), (100, 50))
            pygame.draw.line(screen, (0, 0, 0), (100, 50), (100, 75))
            left.Drawlines()
            pygame.display.flip()
        if a < 3:
            time.sleep(1)
            a += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print('__________________________________________________')
    print(chosenword.display_lines())
    if letters_left == 0:
        print("sorry you lost")
        print('the word was {}'.format(chosenword))
        break
    else:
        want = input('[l] for letter guess, [w] for word guess')
        if want == 'l':
            guess = input('input a letter')
            if checkin(guess) == True:
                print('Correct, no attempts lost')
            elif checkin(guess) == False:
                print('Wrong, you have', letters_left, 'attempts left')
                letters_left -= 1
            elif checkin == 'Already':
                print('You have already guessed that letter')
            if checkwin(guess, str(chosenword)):
                print("congrats you won")
                print('the word was {}'.format(chosenword))
                break
        elif want == 'w':
            guess = input('input a word')
            letters_left -= 1
            if checkwin(guess, str(chosenword)):
                print("congrats you won")
                print('the word was {}'.format(chosenword))
                break
            else:
                print('wrong, you have {} attempts left'.format(letters_left))
