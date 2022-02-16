from random import randint
from time import sleep

x = 0
p1 = 0
p2 = 0
p3 = 0
name_1 = ""
name_2 = ""
name_3 = ""
replay = ""
times_left = 0
num = 1
player_scores = [p1, p2, p3]
player_names = []
player_limits = []
place_switch = 0
dice_array = []
check_array = []


def get_names():
    global num, player_count, turn
    for j in range(0, len(player_scores)):
        player_names[j] = str(input("\nWhat is your name?    \n")).upper()
        print("Hello, " + player_names[j] + "\n")
    for g in range(len(player_names)):
        print("Player " + str(num) + ": " +
              str(player_names[g]).upper() + "\n")
        num += 1
    player_count = len(player_names)
    turn = 3
    roll_die()


def make_die():
    dice_array.append(randint(1, 6))


def replace_die(loc):
    global player_count, spot
    replace = randint(1, 6)
    dice_array[int(loc) - 1] = int(replace)
    print(player_names[int(spot)].upper() +
          ", you rolled a " + str(replace) + "\n")
    for i in range(len(dice_array)):
        print(player_names[int(spot)].upper() +
              " rolled a " + str(dice_array[i]))
    if int(times_left) > 0:
        ask_replace()
    else:
        check_group()
        check_run()
        calc_score()


def ask_replace():
    global times_left, place_switch
    cons = input("Would you like to replace any dice? You can replace " +
                 str(times_left) + " die this turn.     \n")
    if str(cons) == "y" or str(cons) == "yes":
        times_left -= 1
        place_switch = input("Which dice would you like to swap out?     \n")
        if int(place_switch) > 5:
            print("That's not a valid dice number \n")
            place_switch = input("What dice would you like to swap out?     \n")
        replace_die(int(place_switch))
        ask_replace()
    elif str(cons) == "n" or str(cons) == "no":
        check_group()
        check_run()
        calc_score()             


def calc_score():
    global turn, dice_array, x, player_count, spot
    print("Calculating score...\n")
    sleep(1)
    player_scores[int(spot)] = sum(dice_array)
    x = player_scores[int(spot)]
    player_limits[int(spot)] -= x
    print(x)
    if int(player_limits[int(spot)]) > 0:
        print("\n" + player_names[int(spot)].upper() + ", you are now " + str(
            player_limits[int(spot)]) + " points away from reaching the goal of 75!\n")
    else:
        print(player_names[int(spot)].upper() + " reached 75!\n")
        player_names.remove(player_names[int(spot)])
        spot = 2
    dice_array = []
    turn += 1
    roll_die()


def roll_die():
    global times_left, place_switch, player_count, spot, turn
    player_count = len(player_names)
    if player_count == 0:
        replay = input("THE GAME IS OVER \n Would you like to play again?")
        if str(replay).upper() == "YES":
            main()
            return 
        else:
            exit("THANKS FOR PLAYING! ")
    spot = turn % int(player_count)
    for i in range(5):
        make_die()
    times_left = 2
    print("It is " + str(player_names[int(spot)]) + "'s turn.\n")
    print("Rolling dice...\n")
    sleep(2)
    for i in range(len(dice_array)):
        print(player_names[int(spot)].upper() +
              " rolled a " + str(dice_array[i]))
    ask_replace()


def check_group():
    global dice_array, player_scores, turn, spot, player_names, player_limits
    series_count = 0
    temp_bonus = 0
    for u in range(len(dice_array)):
        series_count = dice_array.count(dice_array[u])
        if int(series_count) >= 3:
            temp_bonus += (3 * int(series_count))
            print("\n\nYou have a group of " + str(series_count) +
                  " dice! You will recieve " + str(temp_bonus) + " points!")
            player_limits[spot] -= int(temp_bonus)
            print("\n" + player_names[int(spot)].upper() + ", you are now " + str(
                player_limits[int(spot)]) + " points away from reaching the goal of 75!\n")
            calc_score()
            return True
        elif int(series_count) < 3:
            continue
        elif u == (len(dice_array) - 1) and int(series_count) < 3:
            return False
    if int(series_count) == 0: 
        calc_score()
        return False       


def check_run():
    run_count = 0
    temp_boost = 0
    for g in dice_array:
        if int(g + 1) in dice_array:
            run_count += 1
    if int(run_count) >= 3: 
        temp_boost += (3 * (int(run_count)))
        print("\n\nYou have a run of " + str(int(run_count)) +
                " dice! You will recieve " + str(temp_boost) + " points!")
        player_limits[spot] -= int(temp_boost)
        print("\n" + player_names[int(spot)].upper() + ", you are now " + str(
            player_limits[int(spot)]) + " points away from reaching the goal of 75!\n")
        calc_score()
        return
    elif int(run_count) < 3:
        return


def main():
    global player_limits, player_names
    player_limits = [75, 75, 75]
    player_names = [name_1, name_2, name_3]
    get_names()


main()


# Thesis:

# Given the dissapointing response to the COVID-19 pandemic, the US Public Health System is not prepared to handle future health crises of this magnitude.
