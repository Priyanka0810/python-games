import random
guesses = 0;
number = random.randint(1,100)
while True:
    guess = int(input(f"Enter a no between (1 - 100) : "))
    guesses+=1;
    if guess > number:
        print("too high")
    elif guess < number:
        print("too low")
    else:
        print(f"{guess} is CORRECT!..")
        break;
print(f"it tooks you {guesses} guesses")