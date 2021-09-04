# Description 
# You have planned a dinner with your friends today. It's the right
# time to add them to your program. You need to be sure how
# many friends are joining you for dinner including you.


# The idea is to take names from user input. Store them in a 
# dictionary

# For example, if five friends are joining including you, you need to
# add five people to the dictionary so that you can access/update
# the corresponding bill value later.

# Objectives
# In this stage your program should perform the following steps:
# 1. Take user input - how many people want to join, including
#    the user;
# 2. In case of an invalid number of people (zero or negative),
#    "No one is joining for the party" is expected as an
#    output;
# 3. Otherwise, take the friends' names as input, iteratively;
# 4. Store them in a dictionary initialized with zeros;
# 5. Print out the dictionary

# To communicate with the user, please use the prompts specified
# in the examples. Note that here and in the following stages we
# expect you to take every input in a new line.

# Examples 
# The greatern-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Example 1: Valid input
# Enter the number of friends joining (including you):
# > 5

# Enter the name of every friend (including you), each on a new line:
# > Marc
# > Jem
# > Monica
# > Anna
# > Jason

# {'Marc': 0, 'Jem': 0, 'Monica': 0, 'Anna': 0, 'Jason': 0}

# Example 2: Invalid input
# Enter the number of friends joining (including you):
# > 0

# No one is joining for the party

class BillSplitter:
    
    def __init__(self):
        self.n = None
        self.friends = {}
        
    def take_friends(self):
        print('Enter the number of friends joining (including you):')
        self.n = int(input())
        if self.n > 0:
            print("Enter the name of every friend (including you), each on a new line:")
            [self.friends.update({input(): 0}) for _ in range(self.n)] 
            print(self.friends)
        else:
            print("No one is joining for the party")
    

def main():
    bill_splitter = BillSplitter()
    bill_splitter.take_friends()


if __name__ == "__main__":
    main()

    

        

