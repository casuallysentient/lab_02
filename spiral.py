from karel.stanfordkarel import *


def main():
    spiral()


def spiral():
    """
    This is the master function that executes reach_center, makes Karel turn around, and makes him fill the spiral he just traveled through with beepers.

    pre-condition:  Karel is at (1,1) facing east.
    post-condition: Every available space within the spiral contains a beeper. Karel is standing right outside the exit of the spiral (as in, he took one step out of the spiral) facing east.
    """

    # YOU ARE FREE TO DIVIDE YOUR PROBLEM UP THIS WAY, BUT IF YOU PREFER ANY OTHER WAY, DO WHATEVER MAKES MOST SENSE
    # TO YOU!
    # THE FUNCTION spiral() IS THE ONLY FUNCTION THAT IS REQUIRED FOR THIS PROGRAM TO RUN.
    reach_center()
    turn_around()
    leave_spiral()


def reach_center():
    """
    This is the function that gets Karel to the center of the spiral from his starting position at (1,1).

    pre-condition:  Karel is at (1,1) facing east.
    post-condition: Karel is at the center of the spiral facing the wall at its end. Only one beeper has been placed at the first space inside the spiral so that Karel knows where to stop when he is returning.
    """
    while front_is_clear():
        move()
    turn_left()
    move()
    while front_is_clear() and not left_is_clear():
        move()
    turn_left()
    move()
    put_beeper()

    while front_is_clear() or left_is_clear():
        if front_is_clear():
            move()
        if left_is_clear():
            turn_left()


def leave_spiral():
    """
    This is the function that tells Karel to leave the spiral, placing beepers on all the empty squares inside. He knows to stop when he hits the beeper that he placed at the entrance before, at which point he will stop placing beepers, move one space forward so he is no longer in the spiral, and stop.

    pre-condition:  Karel is at the center of the spiral facing away from the wall at its end. Only one beeper has been placed at the first space inside the spiral so that Karel knows where to stop.
    post-condition: All available spaces in the spiral contain a beeper and Karel is standing right outside the entrance to the spiral facing east.
    """
    while (front_is_clear() or right_is_clear()) and not on_beeper():
        put_beeper()
        if front_is_clear():
            move()
        if right_is_clear():
            turn_right()
    move()


def turn_around():
    """
    Instructs Karel to turn around.

    pre-condition:  Karel is facing any of the four cardinal directions.
    post-condition: Karel will have performed a 180-degree turn.
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Instructs Karel to perform a right turn.

    pre-condition:  Karel is be facing any of the four cardinal directions.
    post-condition: Karel will have performed a 45-degree turn in the RIGHT direction.
    """

    turn_around()
    turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
