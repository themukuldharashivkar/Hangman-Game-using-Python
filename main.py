import random
import words
import art

chosen_word = random.choice(words.word_list)
end_of_game = False
lives = 6

#Import the logo 
print(art.logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blank spaces for the word
display = []
for blank in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    #Check guessed letter
    count = 0
    for letter in chosen_word:
        # print(
        #     f"Current position: {letter}\n Current letter: {letter}\n Guessed letter: {guess}"
        # )
        if letter == guess:
            display[count] = guess
        count += 1
        
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in display:
            print(f"You guessed {guess}, it is not in the word and you lose one life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #print hangman ascii art
    print(art.stages[lives])
