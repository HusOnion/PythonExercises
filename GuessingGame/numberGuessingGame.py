import time
import random

def main():
    print("************************************")
    print("Welcome to the Number Guessing Game!")
    print("************************************")

    is_running = True
    
    while is_running:
        
        guesses = 0


        print("Difficulty levels: Baby (1) , Easy (2), Medium (3), Hard (4), Insane (5) ")

        choice = input("Choose the Difficulty (1,2,3,4,5): ")

        if not choice.isdigit() or int(choice) > 5 or int(choice) < 0:
            print("Invalid Input!")
            continue

        choice = int(choice)

        if choice == 1:
            n = baby(guesses)
            if n == 0:
                break
        
        elif choice == 2:
            easy(guesses)
            

        elif choice == 3:
            medium(guesses)
            

        elif choice == 4:
            hard(guesses)
            

        elif choice == 5:
            insane(guesses)
    
        x = input("Play Again ? (Y for YES , anything for NO): ").upper()
        
        if x == 'Y':
            is_running = True
        else:
            print("Ok bye!")
            is_running = False

    
#__________________________________________________________________________________________________


def baby(guesses):
    number = random.randint(1,10)

    print("Oh hi baby...")
    time.sleep(1)
    print("Baby mode is just to guess a number between 1 and 10 with unlimited guesses...")
    time.sleep(3)
    guess = get_valid_guess(1,10)

    while guess != number:
        
        if guess > number:
            print("Your guess is high")
            guesses += 1
        elif guess < number:
            print("Your guess is low")
            guesses += 1
            
        guess = get_valid_guess(1,10)
    
    print("****************************************************")
    print(f"Nice You Guessed it right the number was {number}")
    time.sleep(1)
    print(f"You took {guesses} guesses")
    print("****************************************************")
    

#__________________________________________________________________________________________________

def easy(guesses):
    number = random.randint(1,100)
    

    print("hi...")
    time.sleep(1)
    print("easy mode is to guess a number between 1 and 100 with unlimited guesses...")
    time.sleep(3)
    guess = get_valid_guess(1,100)

    while guess != number:

        if guess > number:
            print("Your guess is high")
            guesses += 1
        elif guess < number:
            print("Your guess is low")
            guesses += 1
            
        guess = get_valid_guess(1,100)

    print("****************************************************")    
    print(f"Nice You Guessed it right the number was {number}")
    time.sleep(1)
    print(f"You took {guesses} guesses")
    print("****************************************************")

#__________________________________________________________________________________________________

def medium(guesses):
    number = random.randint(1,300)

    print("hi...")
    time.sleep(1)
    print("Ok now the medium mode is to guess a number between 1 and 300")
    time.sleep(2)
    print("but...")
    time.sleep(2)
    print("You will have only 10 guesses!")
    time.sleep(2)
    guess = get_valid_guess(1,300)


    while guess != number and guesses != 10:
        
        if guess > number:
            print("Your guess is high")
            guesses += 1
        elif guess < number:
            print("Your guess is low")
            guesses += 1
            
        guess = get_valid_guess(1,300)
    
    if guesses == 10:
        print("Womp Womp you guessed 10 GUESSES! ")
        time.sleep(1)
        print("Sorry You Lost")
        print(f"The number was {number}")
        return
        
    print("****************************************************")    
    print(f"Nice You Guessed it right the number was {number}")
    time.sleep(1)
    print(f"You took {guesses} guesses")
    print("****************************************************")

#__________________________________________________________________________________________________

def hard(guesses):
    balance = 100
    number = random.randint(1,300)

    print("Ok now we are getting hard! ")
    time.sleep(2)
    print("The hard mode is kinda the same")
    time.sleep(2)
    print("you will guess a number between 1 and 300")
    time.sleep(2)
    print("You will have 10 guesses")
    print("but...")
    time.sleep(2)
    print("and only but...")
    time.sleep(2)
    print("Thier will be a BUDGET!")
    time.sleep(2)
    print("You will have 100$ each wrong guess will cost you MONEY!")
    time.sleep(2)
    print("ALSO, it depends on how far the guess is!!")
    time.sleep(2)
    print(f"Ok lets begin now, Your Balance is ${balance}")
    guess = get_valid_guess(1,300)


    while guess != number:   


        if guess > number:
            if guess - number > 100:
                print("HOLY your guess is way far, -40$ buddy")
                balance -= 40
            elif guess - number > 50:
                print("your guess is too high, -20$")
                balance -= 20
            elif guess - number > 20:
                print("your guess is high, -10$")
                balance -= 10
            elif guess - number > 10:
                print("your guess is kinda high, -5$")
                balance -= 5
            elif guess - number > 3:
                print("Your guess is slightly higher, -2$")
                balance -= 2
            else:
                print("Your guess is closseee, -1$")
                balance -= 1

            guesses += 1

        elif guess < number:
            if number - guess > 100:
                print("HOLY your guess is way low, -40$ buddy")
                balance -= 40
            elif number - guess > 50:
                print("your guess is too low, -20$")
                balance -= 20
            elif number - guess > 20:
                print("your guess is low, -10$")
                balance -= 10
            elif number - guess > 10:
                print("your guess is kinda low, -5$")
                balance -= 5
            elif number - guess > 3:
                print("Your guess is slightly low, -2$")
                balance -= 2
            else:
                print("Your guess is closseee, -1$")
                balance -= 1

            guesses += 1
        

        print(f"Your Balance is ${balance}")
        guess = get_valid_guess(1,300)
    
        if balance <= 0:
            print("NAH YOU ARE BROKE BUDDY!")
            time.sleep(1)
            print(f"Your Balance is {balance}")
            print(f"The number was {number}")
            return
        elif guesses == 10:
            print("Womp Womp you guessed 10 GUESSES! ")
            time.sleep(1)
            print("Sorry You Lost")
            print(f"The number was {number}")
            return  
                
    print("****************************************************")    
    print(f"Nice You Guessed it right the number was {number}")
    time.sleep(1)
    print(f"You took {guesses} guesses")
    print("****************************************************")

#__________________________________________________________________________________________________

def insane(guesses):
    balance = 50
    number = random.randint(1,500)

    print("Ok this is the hardest mode")
    time.sleep(2)
    print("The Insane mode is the same as hard mode but with some tweaks")
    time.sleep(3)
    print("you will guess a number between 1 and 500!")
    time.sleep(2)
    print("You will have 10 guesses")
    print("but...")
    time.sleep(2)
    print("and only but...")
    time.sleep(2)
    print("Thier will be a BUDGET!")
    time.sleep(2)
    print("You will have 50$ each wrong guess will cost you MONEY!")
    time.sleep(3)
    print("ALSO, it depends on how far the guess is!!")
    time.sleep(2)
    print(f"Ok lets begin now, Your Balance is ${balance}")
    guess = get_valid_guess(1,500)


    while guess != number and guesses != 10 and balance != 0:   

        if guess > number:
            if guess - number > 100:
                print("HOLY your guess is way far, -40$ buddy")
                balance -= 40
            elif guess - number > 50:
                print("your guess is too high, -20$")
                balance -= 20
            elif guess - number > 20:
                print("your guess is high, -10$")
                balance -= 10
            elif guess - number > 10:
                print("your guess is kinda high, -5$")
                balance -= 5
            elif guess - number > 3:
                print("Your guess is slightly higher, -2$")
                balance -= 2
            else:
                print("Your guess is closseee, -1$")
                balance -= 1

            guesses += 1

        elif guess < number:
            if number - guess > 100:
                print("HOLY your guess is way far, -40$ buddy")
                balance -= 40
            elif number - guess > 50:
                print("your guess is too low, -20$")
                balance -= 20
            elif number - guess > 20:
                print("your guess is low, -10$")
                balance -= 10
            elif number - guess > 10:
                print("your guess is kinda low, -5$")
                balance -= 5
            elif number - guess > 3:
                print("Your guess is slightly lower, -2$")
                balance -= 2
            else:
                print("Your guess is closseee, -1$")
                balance -= 1

            guesses += 1
        

        print(f"Your Balance is ${balance}")
        guess = get_valid_guess(1,500)
    
    if balance <= 0:
        print("NAH YOU ARE BROKE BUDDY!")
        time.sleep(1)
        print(f"Your Balance is {balance}")
        print(f"The number was {number}")
        return
    elif guesses == 10:
        print("Womp Womp you guessed 10 GUESSES! ")
        time.sleep(1)
        print("Sorry You Lost")
        print(f"The number was {number}")
        return
                
    print("****************************************************")    
    print(f"Nice You Guessed it right the number was {number}")
    time.sleep(1)
    print(f"You took {guesses} guesses")
    print("****************************************************")


def get_valid_guess(min_val, max_val):
    while True:
        guess = input(f"Enter a number ({min_val}-{max_val}): ")
        if not guess.isdigit():
            print("Invalid input. Numbers only.")
            continue

        guess = int(guess)
        if guess < min_val or guess > max_val:
            print("Out of range.")
            continue

        return guess

if __name__ == "__main__":
    main()
