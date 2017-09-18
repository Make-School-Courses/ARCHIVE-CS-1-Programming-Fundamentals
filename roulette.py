'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
random.seed(1)

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet(color, number, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount

def roll_ball():
    '''returns a random number between 0 and 37'''
    pass

def check_results():
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    pass

def payout():
    '''returns total amount won or lost by user based on results of roll. '''
    pass

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:

    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    pass
