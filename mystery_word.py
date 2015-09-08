import random
import sys

guesses = []
current_word = []

def easy_words(words):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_list = []
    for w in words:
        if len(w) > 3 and len(w) < 7:
            easy_list.append(w)
    return easy_list


def medium_words(words):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_list = []
    for w in words:
        if len(w) > 5 and len(w) <9:
            medium_list.append(w)
    return medium_list


def hard_words(words):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_list = []
    for w in words:
        if len(w) > 7:
            hard_list.append(w)
    return hard_list


def random_word(words):
    """
    Returns a random word from the word list.
    """
    return random.choice(words)


def assemble_word(mystery_word, guesses):
    # Loop through mystery word, comparing each letter to the guessed letter.
    display = []
    for letter in mystery_word:
        if letter.upper() in guesses or letter.lower() in guesses:
            display.append(letter.upper())
        else:
            display.append('_')
    return display

def display_word(mystery_word, guesses):
    # Output display of guessed word in progress.
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.
    """
    display = assemble_word(mystery_word, guesses)
    return ' '.join(display)


def is_word_complete(mystery_word, guesses):
    # Checks to see if word has been completed.
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    success = False
    guessed_word = assemble_word(mystery_word,guesses)
    success = ''.join(guessed_word).upper() == mystery_word.upper()
    return success


def play_game(words):
    # Manage setup and the looping of the game.
    level = choose_level()
    mystery_word = set_up_game(level,words)
    win_or_lose = game_loop(mystery_word)
    if win_or_lose == True:
        print("You guessed the word!!  It was " + mystery_word.upper())
    else:
        print("You ran out of guesses!")
        print("\nThe word was " + mystery_word.upper())


def game_loop(mystery_word):
    # Manage game progress until game ends due to win or out of guesses.
    guesses = []
    not_finished = True
    end = False
    chances = 8
    while not_finished:
        print("So far, you have guessed these letters: {} {}".format(guesses, ' '))
        word_display = display_word(mystery_word,guesses)
        print("Here is your word so far: " + word_display)
        guess = get_user_guess(guesses)
        if guess not in mystery_word:
            chances -= 1
        guesses.append(guess)
        is_complete = is_word_complete(mystery_word,guesses)
        if is_complete == True:
            not_finished = False
            end = True
        elif chances == 0:
            not_finished = False
            end = False
    return end

def set_up_game(level,words):
    # Use input level to get mystery word
    mystery_word = ''
    if level in ('E', 'e'):
        mystery_word = random_word(easy_words(words))
    elif level in ('M', 'm'):
        mystery_word = random_word(medium_words(words))
    elif level in ('H' ,'h'):
        mystery_word = random_word(hard_words(words))
    print(("\nGood luck! The word I have chosen for you has {} letters in it.").format(len(mystery_word)))
    return mystery_word


def get_user_guess(guesses):
    # Gets guess from user and checks to see if it has been guessed before.
    guess = ''
    not_yet=True
    while not_yet:
        guess = input("\nPlease guess a letter: ").upper()
        if guess[0] in guesses:
            print("\nYou have already guessed that letter")
        else:
            not_yet=False
    return guess[0]


def choose_level():
    #  Asks user which level of difficulty they want.
    while True:
        level = input("Choose a difficulty level of (E)asy, (M)edium or (H)ard. (Q) = Quit: ")
        if level in ('Q', 'q'):
            print("Maybe we can play some other time.")
            sys.exit(0)
        if level.upper() in ('E', 'M', 'H'):
            break
        else:
            print("Valid choices are E, M, or H")
    return level


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level              #choose_level
    2. Sets up the game based upon the difficulty level     #set_up_game
    3. Performs the game loop, consisting of:               #game_loop
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    words=[]
    with open("/usr/share/dict/words") as f:
        words = f.read()
        words = words.split()
    next_game = True
    while next_game:
        play_game(words)
        play_again = input("Would you like to play again? (Y)es or (N)o: ")
        if play_again[0] not in ('Y', 'y'):
            print("Maybe we can play again some other time.")
            next_game = False


if __name__ == '__main__':
    main()
