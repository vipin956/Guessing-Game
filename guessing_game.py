from random import randint
MAX = 10
while True:
    answer = randint(1, MAX)
    guess = input("Guess a number from 1 to 10: ")
    if guess.isnumeric():
        guess = int(guess)
        if (guess) > 0 and (guess) < 11 and (guess) == answer:
            print("You are a genius 😄")
            break
        elif guess > MAX:
            print("Hey bozo 😠, I said 1 to 10 🤣")
        else:
            print("Wrong guess, it was %d." %(answer))
    else:
        print("Please enter a number.")
        continue
        
