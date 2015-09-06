import random
import sys

def easy_words(words):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    for w in words:
        if len(w) > 3 and len(w) < 7:
            easy_list.append(w)
    return easy_list


def medium_words(words):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    for w in words:
        if len(w) > 5 and len(w) <9:
            medium_list.append(w)
    return medium_list


def hard_words(words):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    for w in words:
        if len(w) > 7:
            hard_list.append(w)
    return hard_list


def random_word(words):
    """
    Returns a random word from the word list.
    """
    return random.choice(words)


def play again():

    print("Congratulations!  You successfully guessed the word!\nWould you like to play again?")
    answer = input(" (Y)es or (N)o: ").lower()
    if answer in ('y', 'yes'):
        choose_level
    else:
        sys.exit(0)
    return


def display_word(mystery_word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.
    """
    guesses.append(guess)
    print("You have {} guesses left.".format(chances))
    print("So far, you have guessed these letters: {} {}".format(guesses, ' '))
    for letter in mystery_word:
        if guess not in guesses
            display.append(letter.upper())
        else:
            display.append('_')
            chances -= 1
    return ' '.join(display)


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    for letter in mystery_word:
        if letter not in guesses:
            win_switch = False
    return win_switch


def set_up_game(level):
    guesses = []    # letters that have been guessed
    chances = 8     # number of allowed guesses
    win_switch = True
    if level in ('E', 'e'):
        mystery_word = random_word(easy_list)
    elif level in ('M', 'm'):
        mystery_word = random_word(medium_list)
    elif level in ('H' ,'h'):
        mystery_word = random_word(hard_list)
    else:
        print("That is not valid input.")
        choose_level()
    print(("\nGood luck! The word I have chosen for you has {} letters in it.").format(len(mystery_word)))
    get_user_guess()
    return(guesses, chances, mystery_word)


def get_user_guess():
    guess = input("\nPlease guess a letter: ").upper()
    if guess in guesses:
        print("\nYou have already guessed that letter")
        get_user_input
    else:
        continue
    return(guess)


def choose_level():
    level = input("Choose a difficulty level of (E)asy, (M)edium or (H)ard. (Q) = Quit: ")
    if level in ('Q', 'q'):
        sys.exit(0)
    else:
        set_up_game
    return(level)


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
    with open("/usr/share/dict/words") as f:
        words = f.read()
        words = words.split()
    choose_level()
    set_up_game(words)
    display_word()


if __name__ == '__main__':
    main()
