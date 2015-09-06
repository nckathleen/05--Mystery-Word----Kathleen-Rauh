import random
import sys
easy_words

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


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    while bad_guess < 8:
        for letter in word:
            if guess in word
                display letter.upper()
            else:
                display = "_ "
                bad_guess += 1
    return


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    if guesses == len(word):
        print("Congratulations!  You guessed the word!\nWould you like to play again?")
        answer = input(" (Y)es or (N)o: ")
        if answer in ('y', 'yes', 'n', 'no'):
            choose_level
        else:
            sys.exit(0)


def set_up_game(mystery_word):
    display = ''
    guesses = []
    wrong = 0
    word_len = len(mystery_word)
    print(("Good luck! The word has {} letters in it.").format(word_len))
    guess = input("Please enter your first letter guess: ").upper()
    guesses = guesses.append(guess)
    return (guesses, word)


def choose_level():
    level = input("Choose a difficulty level of (E)asy, (M)edium or (H)ard. (Q) = Quit: ").lower()
    if level == 'q':
        sys.exit(0)
    elif level == 'e':
        mystery_word = random_word(easy_list)
    elif level == 'm':
        mystery_word = random_word(medium_list)
    elif level == 'h':
        mystery_word = random_word(hard_list)
    else:
        choose_level()
    return(mystery_word)


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level              #choose_level
    2. Sets up the game based upon the difficulty level     #set_up_game
    3. Performs the game loop, consisting of:               #display_word
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


#   #   Set up game using Level, incl a,b,c,d
#   a) rtn = ''
#   for letter in self.word:
#   	if letter not in self.guessed_letters:
#   		rtn += '_'
#   	else:
#   		rtn += letter
#   return rtn
#    b) & c)     def print_game_status(self):
# # #		 while (count != guessedLetter): #while loop to look for the index of the guessed letter
    #         count = count + 1
    #         if (count == guessedLetter): # will go into the board and replace the desired index with the letter if it matches
    #             theBoard[count] = letter
    #             print("The word is: " + ''.join(theBoard))
    #
    # for x in theBoard: # loop to go through theBoard to see if any '*' are there. If none are found it will say you win
    #     if (x != '*'):
    #         win += 1
    # if (win == len(theBoard)):
    #     print("You win!")
#    d)  while True, x = input(make_choice), if bad msg, continue, if 'Q' break
#     # Call approp function for level chosen, passing ??
#


if __name__ == '__main__':
    main()
