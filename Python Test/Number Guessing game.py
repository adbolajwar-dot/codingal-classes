print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 50.")
print("You have 5 attempts to guess the correct number.")

guess = int(input("Please enter your guess: "))

if guess < 1 or guess > 50:
    print("Your guess is out of range. Guess a number between 1 and 50.")
while guess < 50 and guess > 1:
    print("Your almost there! Try to guess the correct number.")
    guess = int(input("Please enter your guess: "))
if guess not in range (1, 51):
 print("You lose one heart.")

elif guess != 23:
    print("Game Over! You've used all your attempts.")

if guess == 23:
    print("Congratulations! You've guessed the correct number!")
else:
    print("Game Over! You've used all your attempts.")

