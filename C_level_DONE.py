from random import randint
from time import sleep

a = 0
b = 0
c = 0
d = 0
e = 0
x = 0
y = 50
times_left = 0
player_score = 0
place_switch = 0
dice_array = []


def make_die():
    dice_array.append(randint(1, 6))


def replace_die(loc):
    replace = randint(1, 6)
    dice_array[int(loc) - 1] = int(replace)
    print("You rolled a " + str(replace))
    print("Your new hand is " + str(dice_array))
    if int(times_left) > 0:
        ask_replace()
    else:
        calc_score()
        main()


def ask_replace():    
    global times_left, place_switch
    cons = input("Would you like to replace any dice? You can replace " + str(times_left) + " die this turn.     ")
    if str(cons) == "y":
        times_left -= 1
        place_switch = input("Which dice would you like to swap out?     ")
        replace_die(int(place_switch))
    elif str(cons) == "n":
        calc_score()
        main()


def calc_score():
    global y
    print("Calculating score...")
    sleep(1)
    x = sum(dice_array)
    y -= x
    print(x)
    if y > 0:
        print("You are now " + str(y) + " points away from reaching the goal of 50!")
        print("")
        print("")
    else:
        exit("You reached the target score!!")
    dice_array = []


def roll_die():
    global times_left, place_switch
    for i in range(5):
        make_die()
    times_left = 2
    print("Rolling dice...")
    sleep(2)
    print("Your hand is " + str(dice_array))
    ask_replace()

def main():
    roll_die()

main()
