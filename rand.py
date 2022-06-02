#import libraries
from random import randint
from time import sleep

x = randint(0,10)

def randomPattern(self):
    if x > 0:
        print(x)
        sleep(x)

if __name__ == "__main__":
    randomPattern(x)
