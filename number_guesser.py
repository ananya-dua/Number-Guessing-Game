import random

def random_guessing_game():
    print("Welcome to the Random Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    num = random.randint(1,100)
    attempts = 1;
        
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts+=1
            
            if guess<num:
                print("Your guess is too low!")
            
            elif guess>num:
                print("Your guess is too high!")
        
            else:
                print("Congratulations! You guessed it in " , attempts , "attempts!")
                break
        
        except ValueError:
            print("Enter a valid number! ")
        
        
    
random_guessing_game()
    
    