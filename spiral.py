from karel.stanfordkarel import *


def main():
    spiral()


def spiral():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
    """

    # YOU ARE FREE TO DIVIDE YOUR PROBLEM UP THIS WAY, BUT IF YOU PREFER ANY OTHER WAY, DO WHATEVER MAKES MOST SENSE
    # TO YOU!
    # THE FUNCTION spiral() IS THE ONLY FUNCTION THAT IS REQUIRED FOR THIS PROGRAM TO RUN.
    reach_center()
    turn_around()
    leave_spiral()


def reach_center():
    """
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
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
    [WRITE YOUR FUNCTION'S DESCRIPTION HERE]

    pre-condition:  [WRITE YOUR PRE-CONDITION HERE]
    post-condition: [WRITE YOUR POST-CONDITION HERE]
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
