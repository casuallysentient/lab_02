from karel.stanfordkarel import *


def pave_all_hurdles():
    """
    This is the master function that gets Karel from one side of the chart to the other and covers the entire chart in a layer of beepers over all the hurdles.

    pre-condition:  Karel is at (1,1) facing north. To his right is the first hurdle. There are no beepers on the board.
    post-condition: Karel has gone over every hurdle, placing a beeper in every position that is anywhere next to a hurdle (including above), and is in the bottom-right corner of the board, facing North with a wall in front of him.
    """

    # YOU ARE FREE TO DIVIDE YOUR PROBLEM UP THIS WAY, BUT IF YOU PREFER ANY OTHER WAY, DO WHATEVER MAKES MOST SENSE
    # TO YOU!
    # THE FUNCTION pave_all_hurdles() IS THE ONLY FUNCTION THAT IS REQUIRED FOR THIS PROGRAM TO RUN.
    while front_is_clear():
        pave_hurdle()
        move_to_wall()
    put_beeper()


def pave_hurdle():
    """
    This is the function that Karel will execute whenever he arrives at the base of a hurdle. When it finishes, it will put a layer of beepers surrounding the hurdle and Karel will be on the other side.

    pre-condition:  Karel is facing north to the left of a hurdle at the bottom.
    post-condition: There is a beeper in every position that Karel occupied while going over the hurdle and Karel is on the other side of the hurdle facing east.
    """
    move_with_wall_on_right()
    put_beeper()
    turn_right()
    move()
    move_with_wall_on_right()
    put_beeper()
    turn_right()
    move()
    move_to_wall()


def move_to_wall():
    """
    This function is used at the end of the pave_hurdle function and then executed again after every instance of said function. The first time it runs in the pave_hurdle function is to get Karel from the top-right corner of the hurdle to the bottom wall, which I chose to do because using the move_with_wall_on_right function for all three sides of the hurdle had the potential to break the function at the end by trying to turn right. The instance of this function that runs after pave_hurdle is executed gets Karel from the bottom-right corner of one hurdle to the next available wall to the east, whether this be the next hurdle or the final wall.

    pre-condition:  Karel is facing a clear path to a wall that does not have any beepers yet. This can be in different directions depending on which instance of this function is running.
    post-condition: Karel has reached the aforementioned wall and turned left, leaving a trail of beepers from where he was before.
    """
    while front_is_clear():
        put_beeper()
        move()
    turn_left()


def move_with_wall_on_right():
    """
    This function is the "up and over" part of the hurdle - it is executed twice in the pave_hurdle function, once to get Karel from the bottom-left to the top-left of the hurdle and again to get Karel from the top-left to the top-right. As long as there is a wall to Karel's right, he will place a beeper and move forward.

    pre-condition:  Karel has a wall to his right and his front is clear with no beepers in his path.
    post-condition: Karel has gone one space past the end of the wall, so there is no longer a wall to his right, and he has left a trail of beepers behind him.
    """
    while not right_is_clear():
        if front_is_clear():
            put_beeper()
            move()


def turn_right():
    turn_around()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def main():
    pave_all_hurdles()


####### DO NOT EDIT CODE BELOW THIS LINE ########


if __name__ == '__main__':
    execute_karel_task(main)
