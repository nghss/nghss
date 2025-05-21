print("Welcome to my trivia quiz!")

playing = input("Do you want to play? ")

# make playing strictly lowercase before checking
if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0 

#Q1
answer = input("What is the colour of an emerald? ")
if answer.lower() == "green":
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!")

#Q2
answer = input("Which Disney movie is Elsa in? ")
if (answer.lower() == "frozen"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

#Q3
answer = input("Where is the Great Pyramid of Giza? ")
if (answer.lower() == "egypt"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

#Q4
answer = input("What do you call a female deer? ")
if (answer.lower() == "doe"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

#Q5
answer = input("What is the largest mammal in the world? ")
if (answer.lower() == "whale"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 
    
#Q6
answer = input("Who is the first man to step on the moon? ").lower()
if (answer == "neil armstrong" or answer == "Neil Armstrong"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

#Q7
answer = input("How many continents are there in the world? ").lower()
if (answer == "seven" or answer == "7"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!")

#Q8
answer = input("What is the fastest land animal? ").lower()
if (answer == "cheetah" or answer == "Cheetah"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

#Q9
answer = input("What is the tallest mountain in the world? Fuji, Kilimanjaro, K2 or Everest? ").lower()
if (answer == "everest" or answer == "Everest"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

#Q10
answer = input("Which capital city of Europe would you find the Eiffel Tower? ").lower()
if (answer == "Paris" or answer == "paris"):
    print('Correct!')
    score += 1
else:
    print("Incorrect, try harder!") 

print("The End! You got " + str(score) + "/10 questions correct!")
print("You got " + str((score/10) * 100) + "%!")

