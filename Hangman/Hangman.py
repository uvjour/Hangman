# Hangman Game
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['microsoft', 'google', 'facebook', 'apple', 'twitter']
chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display.append('_')
word_length = len(chosen_word)
# print('Hint, hint, the chosen word is: ' + chosen_word)
print(display)

lives = 6
i = 0
while i <= 15:
    guess = input("Guess a letter of the word: ")
    guess.lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print('You lose')
            break
    if '_' not in display:
        print('Congratulations! You won!')
        break
    print(display)
    i += 1