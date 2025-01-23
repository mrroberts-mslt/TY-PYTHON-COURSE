# FORK ME or copy the code!  Please don't request edit access. This is the original so it needs to stay undedited for all users.

fruit = ["Apple", "Banana", "Grape", "Strawberry", "Melon", "Orange"]

# Task 1
  # Add comments to predict what the following lines of code will do.

  # Alter the fourth print command so that it outputs a vaild item from the list that hasn't yet been used.

#Output Strawberry
print(fruit[3])
#Output Orange
print(fruit[5])
#Output Apple Grape.  - Make sure students recognise how the space between items was created
print(fruit[0] + " " + fruit[2])
#Out of range error - there is no item at position 6
# Example correction could be print(fruit[4])
print(fruit[4])

# Task 2
  # Write code to output the whole list - you should be able to do this with one line of code.abs

print(fruit)

# Task 3
  # Ask the user to input a number between 0 and 5.  Output the item in the list that matches the number they have input.

usernumber = int(input("Enter a number between 0 and 5"))
print(fruit[usernumber])
