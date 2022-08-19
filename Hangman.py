import random
from hangman_words import word_list
from hangman_arts import stages,logo


print(logo)

chosen_word = random.choice(word_list)

lives = 6


display = []

for _ in range(len(chosen_word)):
    display.append("_")
    
end_of_game = False
    
while not end_of_game :
    guess = input("Guess a letter: ").lower()
    if guess in display :
        print(f"You have already guessed {guess} !")
    for position in range (len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    
    print(f"{' '.join(display)}")
    print(stages[lives])
    
    if lives == 0:
        end_of_game = True
        print("You lose!")
        print(f"The word was {chosen_word}((")
            
  
    if "_" not in display:
        end_of_game = True
        print("You win!")