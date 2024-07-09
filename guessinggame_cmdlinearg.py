from sys import argv
import sys
import random

class negativeInt(Exception):
    pass
    
def enterLevel(prompt):
    while True:
        try:
            inputlevel = int(input(prompt))
            
            if (inputlevel > 0):
                return inputlevel
            else:
                raise negativeInt
        except ValueError:
            pass
        except negativeInt:
            pass



def main():
    level = enterLevel("Level : ")
    random_number = random.randint(1, level)
    print("Random Number : ", random_number)
    while True:
        try:
            guess = int (input("Guess : "))
            if (guess > 0):  
                if (random_number > guess):
                    print("Too small!")
                elif (random_number < guess):
                    print("Too large!")
                else:
                    print ("Just right!")
                    sys.exit()
            else:
                raise negativeInt
        except ValueError:
            pass
        except negativeInt:
            pass

main()