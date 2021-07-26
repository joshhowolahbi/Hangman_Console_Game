import random
from words import words_pack
from visuals import lives_visual
import string


def get_valid_word(words):
    """
    To get a valid word from the words pack without space or hyphen
    :param words: a list of words (word_pack)
    :return: a random word from the words pack
    """
    word = random.choice(words)  # randomly chooses a word from the words list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()  # returns a uppercase of the randomly chosen word


def hangman():
    """
    The Hangman game implementation.
    A randomly selected word from a pack of words is chosen by computer and
    a user is required to guessed the correct letters to make the word.
    :return: None
    """
    word = get_valid_word(words_pack)  # get the randomly selected word
    word_letters = set(word)  # a set of the letters in the word
    alphabets = set(string.ascii_uppercase)  # a set of the alphabets in uppercase
    guessed_letters = set()  # The user's guesses

    lives = 7  # number of lives by player

    # gameplay loop while checking correctly guessed letters and lives left
    while len(word_letters) > 0 and lives > 0:

        # print the number of lives and letters guessed so far
        print('No of lives left: ', lives, '\tLetters guessed already: ', ' '.join(guessed_letters))

        # append correctly guessed letters into list
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print(lives_visual[lives])
        print('Word: ', ' '.join(word_list))

        # user's guess input
        user_guess = input('Guess a letter: ').upper()

        # checking the input validity and handling loop continuity
        if user_guess in alphabets - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print('')

            else:
                lives = lives - 1  # reduce lives by 1 when guessed wrong
                print(f"\nWrong guess, '{user_guess}' is not in the word.")

        elif user_guess in guessed_letters:
            print(f"\n'{user_guess}' have already been guessed. Guess another letter.")

        else:
            print('\nNot a valid letter. Guess a letter from A-Z')

    # after loop exit when all words guessed correctly or when lives == 0
    if lives == 0:
        print(lives_visual[lives])
        print('Hangman dead!. The correct word was: ', word)
    else:
        print(f"Congrats! You guessed the word right: {word}!!")


if __name__ == '__main__':
    response = 'Y'
    # checking if to continue playing game or exit
    while response == "Y" or response == "YES":
        hangman()
        print("")
        response = input("Would you like to play again? (Y/N): ").upper()
        print("")
    else:
        print("Thank You for Playing!")
