#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Define a function to ask#
def ask_name():
    '''Ask name of the user'''
    player_name = (input("Hello! What is your name? "))
    return player_name


# In[2]:


#Define a function to greet#
def greet_player(n):
    '''Greet and ask user'''
    play = (input("Well, " + n + ", think you can a guess a number between 1 and 30 in eight tries? Enter: Yes or No? "))
    return play


# In[3]:


#Define a function to run the game#
def start_game(f, n):
    '''Runs the game with returns from other functions'''
    import random
    winner = random.randint(1, 30)
    number_of_guesses = 0
    if f == "No":
        print("well, I guess it's not for everyone... bye!")
    elif f == "Yes":
        while number_of_guesses < 8:
            guess = input("Guess the number: ")
            guess = int(guess)
            
            number_of_guesses = number_of_guesses + 1
            
            if guess < winner - 5:
                print("Your guess was too low! Try again ")
            elif guess > winner + 5:
                print("Your guess was too high! Try again ")
            elif guess < winner:
                print("Getting warm but still low! Try again ")
            elif guess > winner :
                print("Getting warm but still high! Try again ")
            elif guess == winner:
                print("Yes! ")
                break
    
        if guess == winner:
            print("Nice " + n + "! You've guessed the number in " + str(number_of_guesses) + " guesses.")
        elif guess != winner:
            print("Sorry " + n + "... you did not guess the number. The correct number was " + str(winner))
    
    play_again = input("Would you like to play again? Yes or No? ")
    return play_again
                
            


# In[4]:


def play_true(p, name, m):
    if m == "No":
        print("Ok, bye!")
    elif m == "Yes":
        start_game(p, name)


# In[5]:


#Define the main function#
def main():
    '''Groups all the functions'''
    name = ask_name()
    p = greet_player(name)
    m = start_game(p, name)
    play_true(p, name, m)


# In[6]:


#Run the main function#
main()


# In[ ]:





# In[ ]:




