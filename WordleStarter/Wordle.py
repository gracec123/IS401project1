# File: Wordle.py

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS

def wordle():

    def enter_action(s):
        if len(s) != N_COLS:
            gw.show_message("Please enter a word with {} letters.".format(N_COLS))
            return

        # Check if the entered word is in the predefined dictionary
        if s.upper() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            gw.show_message("Congratulations! You guessed a valid word.")

            # Move to the next row for the next input
            current_row = gw.get_current_row()
            if current_row < N_ROWS - 1:
                gw.set_current_row(current_row + 1)
            else:
                gw.show_message("Game Over! You've reached the maximum number of rows.")

            # Clear letters in the current row
            for col in range(N_COLS):
                gw.set_square_letter(current_row, col, " ")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Test: Select a random word and print it to the console
    solution_word = random.choice(FIVE_LETTER_WORDS)
    print("Randomly chosen word:", solution_word)

if __name__ == "__main__":
    wordle()
