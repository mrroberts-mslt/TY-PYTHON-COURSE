#solution
#Create a list of possible weapons.
weapons = ["sword", "axe", "bat", "smelly cheese", "water pistol"]

# In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
zombieWeakness = weapons[3]

# Output messages telling the user that they have encountered a zombie and should prepare to fight.
print("You are on a lovely walk.")
print("Oh no, a zombie! Not again?!")
print("There is no way to escape.")
print("Prepare to fight!")

# Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  If they type 1 then they should input the weapon name - store it to a new variable. If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
print("Here are the weapons.")
print(weapons)

choice = int(input("Type '1' to pick a weapon from the list or 2 to choose a different weapon."))

if choice == 1:
  weaponChoice = input("Input the weapon you want.")
else:
  weaponChoice = input("Input the new weapon you want.")
  weapons.append(weaponChoice)


# If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  Otherwise output a message saying that they have lost.

if weaponChoice == zombieWeakness:
  print("The zombie speaks.......")
  print("Graaaahhhh!  You have found my weakness! Curse you and your " + weaponChoice +"!")
  print("Congratulations, you have won the fight.")
else:
  print("The zombie speaks.......")
  print("Graaaahhhh!  Your puny " + weaponChoice + " is no match for me!  Brains! Braaaaiiiinnnnnnssssss......")
  print("You have lost the fight, prepare to be eaten!")


