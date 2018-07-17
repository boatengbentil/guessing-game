
import time
import RPi.GPIO as G
import random


name = raw_input("\n What is your name, dear friend?       ")
name = name.capitalize()
print "Welcome " + name + "."

print "\n " + name + ", you may start guesing \n"
diction = ["embezzlement", "bibliography", "conjunctival", "workmanships", "zooplanktons", "UNAFFORDABLE", "TRANSCENDENT", "transgressor", "submergement","abbreviation", "equalization", "extravaganza", "extempoxrized", "tranquilized", "abominations"]
sec_word = random.choice(diction)

guesses = random.sample(sec_word, 3)


G.setwarnings(False)

G.setmode(G.BOARD)
G.setup(7, G.OUT)
G.setup(3, G.OUT)
G.output(3, False)




no_of_life = 7

while no_of_life != 0:
    failed = 0
    
    for letter in sec_word:
        if letter in guesses:
            
            print letter,
        else:
            
            print "_",
            failed += 1
    if failed == 0:
        print "\n"
        print "\n You won."
        
        G.output(7, True)
        time.sleep(5)
        G.output(7, False)
        #time.sleep(.02)
            
        no_of_life == 0
        break

    guess = raw_input("\n\n Guess the next character:           ")
    guesses += guess
    if guess not in sec_word:
        no_of_life = no_of_life - 1
        G.output(3, True)
        time.sleep(1)
        G.output(3, False)
        if no_of_life == 0:

            
            #time.sleep(.02)
            
            print "You lose"
            G.output(3, True)
            time.sleep(5)
            G.output(3, False)
            
        else:
            print "\n You were wrong, you still have " + str(no_of_life) + " lives"
            

