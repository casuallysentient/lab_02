from karel.stanfordkarel import *


def main():
    pick_up_top_beepers()


def check_line():
    while front_is_clear():
        move()
        if on_beeper():
            if front_is_clear():
                pick_beeper()
    turn_left()


def pick_up_top_beepers():
    check_line()
    check_line()
    check_line()
    check_line()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
