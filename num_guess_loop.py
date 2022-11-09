#!/usr/bin/env python3
# Created by: Patrice Pat-Odita
# Created on: Nov, 9 2022
# This program asks the user to guess a
# number between 0-9 and checks if the user followed instructions
# and then loops it if the instructions are not followed.
import random


def main():
    # initialize the counter
    counter = 0
    # Generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    while True:
        # Get user input
        user_num_string = int(input("Enter a positive number from 0-9: "))
        print()
        # Try catch invalid input
        try:
            # Changing string to integer
            user_num = int(user_num_string)
            # Check if number input is positive
            if user_num < 0 or user_num > 9:
                print("Enter a number from 0-9")
                # Increment counter
                counter = counter + 1
            if user_num == random_number:
                # Display result to user
                print()
                print("{} You guessed, good job!".format(user_num))
                break

            else:
                # Display result to user
                print("{} You guessed wrong".format(user_num))
            print()
            print("Tracking {0} times through the loop.".format(counter))
            print()
        except Exception:
            print("{} This is not an integer.".format(user_num_string))
            print()

    print()
    print("\033[1;35;38mThanks for playing")


if __name__ == "__main__":
    main()
