import random
randNumber= random.randint(1,100)

userGuess= None
guesses= 0
while( userGuess != randNumber):
    userGuess= int(input("Enter your guess"))
    guesses += 1
    if( userGuess == randNumber):
        print("You guressed it right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Enter the smaller Number")
        else:
            print("You guessed it wrong! Enter the larger Number")

print(f"You guessed the number in {guesses} guesses.")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("You have just broken the high Score")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))


    
