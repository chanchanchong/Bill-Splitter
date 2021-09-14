# Description
# It's bill time! Let's split the bill among everyone and update 
# the values in teh dictionary you have created in the previous
# stage.

# Since we don't want to deal with too many decimals (who
# carries that much change anyway?), round the split amount
# to two decimal places and then update the dictionary with
# the split values.

# Objectives
# In this stage your program should perform the followgin
# steps together with the steps of the previous stage:
# 1. If there are no people to split the bill (the number of
#    friends is 0 or an invalid input), output "No one is
#    joining for the party";
# 2. Else, take user input: the final bill;
# 3. Split the total bill equally among everyone;
# 4. Round the split value to two decimal places;
# 5. Update the dictionary with the split values;
# 6. Print the updated dictionary.

# Do not print the output of the previous stage (see examples).

# Examples 
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of the input.

# Example 1: Five people joining
# Enter the number of friends joining (including you):
# > 5

# Enter the name of every friend (including you), each on a new line.
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason

# Enter the total bill value:
# > 100

# {'Marc': 20, 'Jem': 20, 'Monica': 20, 'Anna': 20, 'Jason': 20}

# Example 2: Seven people joining
# Enther the number of friends joining (including you):
# > 7

# Enter the name of every friend (including you), each on a new line.
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason
# > Ben
# > Ned

# Enter the total bill value:
# > 41

# {'Marc': 5.86, 'Jem': 5.86, 'Monica': 5.86, 'Anna': 5.86, 'Jason': 5.86, 'Ben': 5.86, 'Ned': 5.86}

# Example 3: Invalid input
# Enter the number of friends joining (including you):
# > 0

# No one is joining for the party

class BillSplitter:

    def __init__(self):
        self.n = None
        self.friends = {}
        self.bill = None

    def take_friends(self):
        print("Enter the number of friends (including you), each on a new line.")
        try:
            self.n = int(input())
            assert self.n > 0
        except AssertionError:
            print("No one is joining for the party")
        else:
            print("Enter the name of every friend joining (including you):")
            [self.friends.update({input(): 0}) for _ in range(self.n)]
            print("Enter the total bill value: ")
            self.bill = int(input())
            each_bill = round(self.bill / self.n, 2) if (self.bill / self.n) % 1 != 0 else round(self.bill / self.n)
            for f in self.friends:
                self.friends[f] = each_bill
            print(self.friends)


def main():
    bill_splitter = BillSplitter()
    bill_splitter.take_friends()


if __name__ == "__main__":
    main()
