from words import WordList
import random
import time
wrong = 0
word = random.choice(WordList) # will choose a random word from our imported list 
print(word) #testing purposes
# Create a display version with underscores
word_update = ["_" for _ in word]

# Function that will update the word update the blanks the random word
def show_letters(letter):
    global word_update
    for index, char in enumerate(word):
        if char == letter:
            word_update[index] = letter

Username = str(input("Enter your name to play: "))
print("Are you ready to play" + Username + "?")
time.sleep (1)
print("Time to guess the word.")

playing = True #Put a playing status so I can make a false output on some conditions to stop the game

while "_" in word_update:
    print(" ".join(word_update))
    guess = input("Enter a letter: ")
    
    if len(guess) == 1 and guess.isalpha():  # Check if input is a single letter
        if guess in word:
            show_letters(guess) #If the guess is in the word, it will update our index for the word filling it up every time we guess a wrod
        else:
            print("Incorrect guess.")
            wrong += 1            #Mistake increment

            if wrong == 3:        #Condition for max wrong guesses
                print("Sorry, you've run out of guesses. You lose.")
                playing == False #Stops the game

    else:
        print("Please enter a valid single letter.")

if "_" not in word_update:        #Every time we guess a correct letter, it replaces _ with the *letter*. When the index doesn't have "_" anymore, it means we guessed all letters
    print("Congratulations! You've guessed the word: " + ''.join(word_update))
    
#Asking to play again
again = int(input("Would you like to play again? 1 for yes, 2 for no: "))  

if again == 1:                
    play = True #executes the loop to play again
               
elif again == 2:
    print("Thank you for playing Hangman")
    play = False #Stops the game
 