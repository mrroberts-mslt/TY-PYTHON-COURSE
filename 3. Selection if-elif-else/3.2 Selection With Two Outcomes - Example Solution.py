# FORK ME or copy the code!  Please don't request edit access. This is the original so it needs to stay undedited for all users.

# Task 1

# Add comments to the code to explain:
  # What will be output when the code is run?
  # In what circumstances would the other output message be produced

num1 = 42

# The output will be 'You have discovered the meaning of life'.  To get the other output the num1 variable would have to have a number other than 42 stored in it.
if num1 == 42:
  print("You have discovered the meaning of life!")
else:
  print("Sorry, you have failed to discover the meaning of life!")


# Task 2

# Add to the code below so that it outputs 'You're not Dave!' if the user does not input 'Dave'

name = input("What's your name?")

if name == "Dave":
  print("Hello Dave")
else:
  print("You're not Dave!")


  #EXTRA CHALLENGE - Adapt the code so that it works in the same way but uses a not equal to Boolean operator.

name = input("What's your name?")
# Operator changed to not equal to and I've reversed the order of the print statements too so that it is logically correct.
if name != "Dave":
  print("You're not Dave!")

else:
  print("Hello Dave")

# Task 3 - Secret Pass Cod

# Write a program that:
  # Stores the number 1337 in a variable called 'passCode'
  # Asks the user to guess the 4 digit pass code and stores their input in a new variable (you choose the name)
  # If the user inputs 1337 then output 'Pass code correct', otherwise output 'Pass code incorrect'

passCode = 1337

# Input converted to integer
guess = int(input("Guess the 4 digit pass code"))

# Comparing two variables in the condition
if guess == passCode:
  print("Pass code correct")
else:
  print("Pass code incorrect")

# Task 4 - Biggest number

  # Write a program that:
    # Asks the user to input two different numbers and stores them in two variables.
    # Outputs the biggest number entered


# Make sure students use two separate variables. Lots forget this
num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))

if num1 > num2:
  # num1 data converted to string for output
  print(str(num1))
else:
  print(str(num2))

  # Get students to run this code several times to test it.  Some may spot that it doesn't work properly for two numbers that are the same.  For that we need a third outcome, which leads us nicely on to the next set of activities.
