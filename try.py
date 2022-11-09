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
    # generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    while True:
        # Get the user number as string
        user_number_string = input("Enter a whole number between 0 and 9: ")
        try:
            # Changing string to integer
            user_number = int(user_number_string)
            # Check to see if they inputed a postive number
            if user_number >= 0 and user_number <= 9:
                # Increment counter
                counter = counter + 1
                if user_number == random_number:
                    # Display result to user
                    print()
                    print("{} is correct, good job!".format(user_number))
                    break
                else:
                    # Display result to user
                    print("{} is incorrect".format(user_number))
                    print()
                    print("Tracking {0} times through the loop.".format(counter))
                    print()
            else:
                print("This number is not between 0 and 9")
                print()
        # Catches any exeptions
        except Exception:
            print("{} is invaild.".format(user_number_string))
            print()


if __name__ == "__main__":
    main()
