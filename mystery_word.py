

import random
easy_words



def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """

    for w in word_list:
        if len(w) >= 4 and len(w) <= 6:
            list.append
    return list

    # TODO  choose only 4-6 letter words
    #   randomly choose one word to pass

    # TODO
    pass



def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """


    for w in word_list:
        if len(w) >= 6 and len (w)<= 8:
            list.append
    return list


    # TODO
    pass


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """


    for w in word_list:
        if len(w) >= 8:
            list.append
    return list


    # TODO
    pass


def random_word(word_list):
    """
    Returns a random word from the word list.
    """

    word = random.choice(list)
    return list


    # TODO
    pass


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

    # TODO
    pass


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # TODO
    pass


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

    f = open("/usr/share/dict/words")
    word_list = f.read
    print(word_list(10))

    level = input("Choose a difficulty level of (E)asy, (M)edium or (H)ard: ")

    if level == 'E':
        easy_word(word_list)
    elif level = 'M':
        medium_word(word_list)
    else:
        hard_word(word_list)


#     # TODO
#     #

#
#     # Set up game using Level, incl a,b,c,d
    c)
#   d)  while True, x = input(make_choice), if bad msg, continue, if 'Q' break
#     # Call approp function for level chosen, passing ??
#     #
#     f.close
#
# if __name__ == '__main__':
#     main()

    # TODO


if __name__ == '__main__':
    main()
