
# Task 1
countries = ["UK", "USA", "Chad", "Australia", "Thailand"]

# Add comments to the code to explain what the following lines do.

# Replaces 'Australia' with 'Mexico'
countries[3] = "Mexico"
# Replaces 'UK' with #'Iceland'
countries[0] = "Iceland"
# Replaces 'USA' with 'Thailand'
countries[1] = countries[4]

# Add comments to predict what the list looks like now.
  # Iceland, Thailand, Chad, Mexico, Thailand

# Add a line of code to print the whole list and check your prediction
print(countries)

# Task 2

squareNumbers = [1,4,9,16,25,36]

# Add comments to explain what the following lines of code do. 

# Replaces 36 with 49
squareNumbers[5] = 49

# Adds one to 1
squareNumbers[0] +=1

# Calculates 16 - 2 and stores the result in the total variable
total = squareNumbers[3] - squareNumbers[1] 
print (total)

# Add comments to predict what the list looks like now.
  # 2,4,9,16,25,42

# Add a line of code to print the whole list and check your prediction
print(squareNumbers)
