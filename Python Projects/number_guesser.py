import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print("Please type a number larger than 0 next time.")
        quit()
else: 
    print("please type a number next time.")
    quit()

r = random.randint(0, top_of_range) # from 0, does include the number they gave
guesses = 0 

while True: 
    guesses += 1 # increment guesses
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else: 
        print("Please type a number next time.")
        continue # brings you to top of the loop 

    if guess == r:
        print("You got it!")
        break
    elif guess > r: 
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses") 

    
