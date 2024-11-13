
num1 = int(input("Enter a number 10 or less"))

while num1 > 10:
  #I've combined the first two sub tasks in this one line. 
  num1 = int(input("You didn't enter a number less than 10. Please try again."))

print("Thank you, you typed " + str(num1))


# Task 3

  # Write a program that stores a secret number in a variable (you decide the number and the name of the variable)
  # The user has to guess the secret number, the program should loop until they get it right.
  # Once the user has guessed correctly they get a congratulations message

secretNumber = 7

guess = int(input("Guess the secret number"))

while guess != secretNumber:
  guess = int(input("Incorrect! Try again."))

print("Congratulations!")
