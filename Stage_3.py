# Stage 3/4: The Lucky One
# Description

# In this stage, you need to add a new feature to the project
# pick one name from the dictionary at random; this person's
# share will be paid by other. Make it a lucky day for
# somebody!

# Make sure you give your users a choice whether they want to
# use this feature or not. Don't turn it on by default.

# After picking a random name, print it so that everyone knows
# who is the lucky one.

# Objectives

# In this stage your program should perform the following
# steps together with the steps from the previous stages:

# 1. In case of an invalid number of people, "No one is
#    joining for the party" is expected as an output;
# 2. Otherwise, ask the user whether they want to use the
#    "Who is lucky?" feature;
# 3. Take input from the user;
# 4. If a user wants to use the feature (Yes), choose a
#    name from the dictionary keys at random and print
#    the following: {Name} is the lucky one!;
# 5. If the user enters anything else, print No one is
#    going to be lucky.

# Do not print the output of the previous stage (see examples).

# Examples

# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of the input.

# Example 1: The feature is used
# Enter the number of friends joining (including
# you):
# > 5

# Enter the name of every friend (including you),
# each on a new line:
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason

# Enter the total bill value:
# > 100

# Do you want to use the "Who is lucky?" feature?
# Write Yes/No:
# > Yes

# Jem is the lucky one!

# Example 2: The feature is skipped

# Enter the number of friends joining including
# you):
# > 5

# Enter the name of every friend (including you),
# each on a new line:
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason

# Enter the total bill value:
# > 100

# Do you want to use the "Who is lucky?" feature?
# Write Yes/No:
# > No

# No one is going to be lucky

# Example 3: Invalid input

# Enter the number of friends joining (including
# you):

# No one is joining for the party
import random


class BillSplitter:
    def __init__(self):
        self.n = None
        self.friends = {}
        self.bill = None

    def take_friends(self):
        print('Enter the number of friends joining (including you):')
        try:
            self.n = int(input())
            assert self.n > 0
        except AssertionError:
            print("No one is joining for the party")
        else:
            print("Enter the name of every friend (including you), each on a new line:")
            [self.friends.update({input(): 0}) for _ in range(self.n)]
            print("Enter the total bill value:")
            self.bill = int(input())
            each_bill = round(self.bill / self.n, 2) if (self.bill / self.n) % 1 != 0 else round(self.bill / self.n)
            for f in self.friends:
                self.friends[f] = each_bill

            print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
            answer = input()
            print(random.choice([_ for _ in self.friends]) + " is the lucky one!"
                  if answer == "Yes"
                  else "No one is going to be lucky")


def main():
    bill_splitter = BillSplitter()
    bill_splitter.take_friends()


if __name__ == "__main__""":
    main()
