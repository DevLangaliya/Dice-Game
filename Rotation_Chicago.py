from random import randint
from time import sleep
import sys

sys.setrecursionlimit(9999)

x = 0
y = 50
p1 = 0
p2 = 0
p3 = 0
name_1 = ""
name_2 = ""
name_3 = ""
replay = ""
times_left = 0
num = 1
round_num = 1
player_scores = [p1, p2, p3]
player_names = []
player_limits = []
place_switch = 0
dice_array = []
check_array = []
chi_scores = []


def get_names2():
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
    roll_die2()


def make_die2():
    dice_array.append(randint(1, 6))


def replace_die2(loc):
    global player_count, spot
    replace = randint(1, 6)
    dice_array[int(loc) - 1] = int(replace)
    print(player_names[int(spot)].upper() +
          ", you rolled a " + str(replace) + "\n")
    for i in range(len(dice_array)):
        print(player_names[int(spot)].upper() +
              " rolled a " + str(dice_array[i]))
    if int(times_left) > 0:
        ask_replace2()
    else:
        check_group2()
        check_run2()
        calc_score2()


def ask_replace2():
    global times_left, place_switch
    cons = input("Would you like to replace any dice? You can replace " +
                 str(times_left) + " die this turn.     \n")
    if str(cons) == "y" or str(cons) == "yes":
        times_left -= 1
        place_switch = input("Which dice would you like to swap out?     \n")
        if int(place_switch) > 5:
            print("That's not a valid dice number \n")
            place_switch = input(
                "What dice would you like to swap out?     \n")
        replace_die2(int(place_switch))
        ask_replace2()
    elif str(cons) == "n" or str(cons) == "no":
        check_group2()
        check_run2()
        calc_score2()


def calc_score2():
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
    roll_die2()


def roll_die2():
    global times_left, place_switch, player_count, spot, turn
    player_count = len(player_names)
    if player_count == 0:
        replay = input("THE GAME IS OVER\nWould you like to play again?")
        if str(replay).upper() == "YES":
            main2()
            return
        else:
            print("\nTHANKS FOR PLAYING!\n")
            main3()
    spot = turn % int(player_count)
    for i in range(5):
        make_die2()
    times_left = 2
    print("It is " + str(player_names[int(spot)]) + "'s turn.\n")
    print("Rolling dice...\n")
    sleep(2)
    for i in range(len(dice_array)):
        print(player_names[int(spot)].upper() +
              " rolled a " + str(dice_array[i]))
    ask_replace2()


def check_group2():
    global dice_array, player_scores, turn, spot, player_names, player_limits
    series_count = 0
    temp_bonus = 0
    for u in range(len(dice_array)):
        series_count = dice_array.count(dice_array[u])
        if int(series_count) >= 3:
            temp_bonus += (3 * int(series_count))
            print("\n\nYou have a group of " + str(series_count) +
                  " dice! You will receive " + str(temp_bonus) + " points!")
            player_limits[spot] -= int(temp_bonus)
            print("\n" + player_names[int(spot)].upper() + ", you are now " + str(
                player_limits[int(spot)]) + " points away from reaching the goal of 75!\n")
            calc_score2()
            return True
        elif int(series_count) < 3:
            continue
        elif u == (len(dice_array) - 1) and int(series_count) < 3:
            return False
    if int(series_count) == 0:
        calc_score2()
        return False


def check_run2():
    run_count = 0
    temp_boost = 0
    for g in dice_array:
        if int(g + 1) in dice_array:
            run_count += 1
    if int(run_count) >= 3:
        temp_boost += (3 * (int(run_count)))
        print("\n\nYou have a run of " + str(int(run_count)) +
              " dice! You will receive " + str(temp_boost) + " points!")
        player_limits[spot] -= int(temp_boost)
        print("\n" + player_names[int(spot)].upper() + ", you are now " + str(
            player_limits[int(spot)]) + " points away from reaching the goal of 75!\n")
        calc_score2()
        return
    elif int(run_count) < 3:
        return


def main2():
    global player_limits, player_names
    player_limits = [75, 75, 75]
    player_names = [name_1, name_2, name_3]
    get_names2()


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
    cons = input("Would you like to replace any dice? You can replace " +
                 str(times_left) + " die this turn.     ")
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
        print("You are now " + str(y) +
              " points away from reaching the goal of 50!\n\n")
    else:
        print("You reached the target score!!\n")
        main3()
    dice_array = []


def roll_die():
    global times_left, place_switch
    for i in range(5):
        make_die()
    times_left = 2
    print("Rolling dice...\n")
    sleep(2)
    print("Your hand is " + str(dice_array))
    ask_replace()


def main():
    roll_die()


def enter_names(reps):
    global player_names, turn, spot, chi_scores


def roll_die3():
    dice_array.append(randint(1,6))


def commands(inputs):
    if str(inputs).upper() == 'H':
        print("\n'b': runs the B-level dice game\n")
        print("'c': runs the C-level dice game\n")
        print("'chi' or 'r': runs the game 'Chicago', AKA 'Rotation'\n")
        print("'e': Exits the program\n")
        main3()
    elif str(inputs).upper() == 'B':
        main2()  
    elif str(inputs).upper() == 'C':     
        main()
    elif str(inputs).upper() == 'E':
        exit("\nSee you soon!\n\n\n")
    elif str(inputs).upper() == 'CHI' or str(inputs).upper() == 'R':
        # print("This is currently under reconstruction\n\n")
        # main3()
        players = input("\nHow many players do you want to play with?\n")
        enter_names(int(players))
    else:
        print("\nThat is not a valid command! Please try again.\n")
        main3()


def main3():
    value = input("What would you like to do? Enter 'h' to see all available options.\n")
    commands(str(value))


main3()
