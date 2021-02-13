from karel.stanfordkarel import *


def main():
    infinite_loop()


def infinite_loop():
    """
    This function is designed to trap Karel in an infinite loop around a block in the center of the track. After starting to move, as long as the front is clear and the left is blocked, Karel will move forward until he reaches the end of a wall (i.e., the point at which the left is no longer clear), at which point he will turn left and continue moving forward. He will repeat this process as long as you allow the function to continue.

    pre-condition:  Karel is in the position (1,1) facing east with the front clear.
    post-condition: Karel is in an infinite loop, moving forward along a wall to his left until he reaches the end, when he will turn left and continue, repeating this process until you stop the function.
    """
    while front_is_clear():
        move()
        if left_is_clear():
            turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
