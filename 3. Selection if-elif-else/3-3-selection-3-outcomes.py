#COPY THE CODE
 # Task 1

 # 1. Add comments to explain the overall job of the program.
 # 2. Add comments to the code to explain the circumstances that would produce each output

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
  print (num1, " is bigger.")
elif num1 < num2:
  print (num2, " is bigger")
else:
  print("The numbers are the same")

 # EXTRA CHALLENGE - Why do we not need a condition after the 'else'?



# Task 2

# 1. Add an elif to the program so that if the user inputs 'Music' they get a message saying 'Not bad, but Computing is better'.
# 2. Use else For all other subjects the user should get a message saying 'How wrong can you be? Computing is waay better than that!'

subject = input("What's the best school subject?")

if subject == "Computing":
  print("That is the right answer!")
elif subject == "computing":
  print("You are correct, but Computing starts with a capital 'C' ")


# Task 3 - Which room

  # 1. Write a program that asks the user for their name and which subject they are studying.

  # 2. The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.

  # Example - for input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'
 
