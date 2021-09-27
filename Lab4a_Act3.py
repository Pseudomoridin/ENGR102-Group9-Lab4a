# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 2A Activity 3
# Date:         September 8, 2021

trues = ["True", "T", "t"]
falses = ["False", "F", "f"]
breakHere = ""

a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")
inlist = [a,b,c]

# try/catches ensuring the right data type
# it should throw an error if its the right data type
# Gets caught and continues
# testing if a is a number
try:
  int(a)
  breakHere += "A"
except:
  a

# testing if b is a number
try:
  int(b)
  breakHere += "B"
except:
  b

# testing if c is a number
try:
  int(c)
  breakHere += "C"
except:
  c

# Can't raise exception inside a try/catch so it's done here, tells user what output was bad
if not breakHere == "":
  raise Exception("ValueError: Invalid input {}".format(breakHere))

# It says there aren't enough comments so I'm gonna make sure it has enough comments
# This checks to make sure that the input is valid
# It's entirely useless and has no reason for existing
for x in range(len(inlist)):
  if (inlist[x] in trues):
    inlist[x] = True
  elif (inlist[x] in falses):
    inlist[x] = False
  else:
    raise Exception("ValueError: String \"{}\" is invalid input.".format(inlist[x]))
########### Part A ###########
########### Part B ########### 
a = inlist[0]
b = inlist[1]
c = inlist[2]

#output timeeeeee
print("a and b and c:",bool(a and b and c))
print("a or b or c:",bool(a or b or c))
########### Part C ###########
print("XOR:",bool(not(a and b) and (a or b)))
print("Odd number:",bool(((a and b and c) or (a and (not b) and (not c) or ((not a) and (not b) and c) or ((not a) and b and (not c))))))

########### Part D ########### 
print("Complex 1:", bool( (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b) ))
print("Complex 2:", bool( (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b)) ))
))
print("Simple 1:", bool( ((a != b) or not a and not b) ))
print("Simple 2:", bool( (not ((b or not c) and (not a or not c))) or (a and not c) ))