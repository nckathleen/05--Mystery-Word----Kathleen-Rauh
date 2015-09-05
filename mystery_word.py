import random
easy_words

def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    for w in word_list:
        if len(w) > 3 and len(w) < 7:
            list.append
    return list


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    for w in word_list:
        if len(w) > 5 and len(w) <9:
            list.append
    return list


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    for w in word_list:
        if len(w) > 7:
            list.append
    return list


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    return random.choice(word_list)



def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """

    return


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """

def set_up_game(list):
word_len = len(word)
print("The word has {} letters in it.").format(len(word))
    guess = input("Please enter your first letter guess: ")


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    with open("/usr/share/dict/words") as f:
        word_list = f.read()
        word_list = word_list.split()
    get_input()
    set_up_game(word_list):


    def get_input()
        level = input("Choose a difficulty level of (E)asy, (M)edium or (H)ard: ")
        if len(level) > 1:
            print("You must choose (E), (M) or (H).  You can enter Q to quit the game.")
            get_input
        if level == 'E':
            easy_word(word_list)
        elif level == 'M':
            medium_word(word_list)
        elif:
            hard_word(word_list)
        else:
            break


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
#     #
#     f.close
#
# if __name__ == '__main__':
#     main()

    # TODO


if __name__ == '__main__':
    main()
