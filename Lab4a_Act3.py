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

a = input("bool1: ")
b = input("bool2: ")
c = input("bool3: ")
inlist = [a,b,c]
try:
  int(a)
  breakHere += "A"
except:
  a

try:
  int(b)
  breakHere += "B"
except:
  b

try:
  int(c)
  breakHere += "C"
except:
  c

if not breakHere == "":
  raise Exception("ValueError: Invalid input {}".format(breakHere))

for x in range(len(inlist)):
  if (inlist[x] in trues):
    inlist[x] = True
  elif (inlist[x] in falses):
    inlist[x] = False
  else:
    raise Exception("ValueError: String \"{}\" is invalid input.".format(inlist[x]))

#part B
a = inlist[0]
b = inlist[1]
c = inlist[2]

print(bool(a and b and c))
print(bool(a or b or c))
#part C
print(bool(not(a and b) and (a or b)))
print(bool())
