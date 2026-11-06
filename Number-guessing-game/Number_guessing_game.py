import random
print("===NUMBER GUESSING GAME===")
secret_number = random.randint(1, 100)
attempts = 3 
print("I am thinking of a number between 1 and 100.")
print("You have 3 attempts to guess the number.")
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("congratulations! You guessed the number correctly.")
        break
    elif guess > secret_number:
        print("You guess is too high!")
    else:
        print("Your guess is too low!")
        attempts = attempts - 2
        if attempts > 0:
            print("you have", attempts, "attempts left.")
        else:
            print("Game over! The number was",secret_number)
            secret_number = 7
attempts = 3
print("I am thing of a number between 1 and 10. You have 3 attempts to guess it.")
print("You have 3 attempts to guess the number.")
while attempts > 0:
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly!")

        break
    elif guess > secret_number:
        print("Your guess is too high!")
    else: 
        print("Your guess is too low!")
        attempts = attempts - 1
        if attempts > 0 and guess != secret_number:
            print("You have", attempts, "attempts left.")
        elif attempts == 0 and guess != secret_number:
            print("Game over! The number was", secret_number)

