# ================================
# NUMBER GUESSING GAME
# ================================

# ---------- SETTINGS (given to you) ----------
secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ---------- PART 1: the loop and the guess ----------
# YOUR CODE HERE
# Write a while loop that runs while count is less than max_attempts
# AND guess is not equal to secret.
# Inside the loop (indented):
#   read the guess with int(input("Your guess: "))
#   add 1 to count

    # ---------- PART 2: win or not ----------
    # YOUR CODE HERE
    # If guess equals secret, print a win message.
    # Otherwise (else), do Parts 3 and 4.

        # ---------- PART 3: distance and hint ----------
        # YOUR CODE HERE
        # Work out diff, the distance between guess and secret.
        # Do not use abs(). Use if / else instead.
        # Print a hint:  diff >= 20 Ice cold | diff >= 10 Cold | diff >= 5 Warm | else Hot

        # ---------- PART 4: lives left ----------
        # YOUR CODE HERE
        # remaining = max_attempts - count
        # If remaining is more than 0, use a for loop to print a ❤️ for each life left.

# ---------- GAME OVER (after the loop) ----------
# YOUR CODE HERE
# If guess is still not equal to secret, print "Game over"
# and show the secret number.
