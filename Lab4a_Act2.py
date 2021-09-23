1# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 2A Activity 3
# Date:         September 8, 2021

a = str(input("Please enter the coefficient A: "))
b = str(input("Please enter the coefficient B: "))
c = str(input("Please enter the coefficient C: "))

squaredString = "x^2"
xString = "x"
constant = ""
stringFinal = ""

#handling a, different from others 
if (abs(int(a)) != int(a)):
  if (abs(int(a)) == 1):
    squaredString = "- " + squaredString
    a = ""
  else:
    squaredString = "- " + a[1:] + squaredString
    a = ""
elif (int(a) == 1):
  a = ""
try:
  if int(a) == 0:
    squaredString = ""
  else:
    squaredString = a + squaredString
except:
  a

#standardized method for b and c
if int(b) == 0:
  b = ""
  xString = ""
elif abs(int(b)) == 1:
  if abs(int(b)) != int(b):
    b = " - "
  else:
    if (squaredString != ""):
      b = " + "
elif abs(int(b)) != int(b):
  b = " - " + b[1:]
else:
  if squaredString != "":
    b = " + " + b
xString = b + xString

if int(c) == 0:
  c = ""
  constant = ""
elif abs(int(c)) != int(c):
  c = " - " + c[1:]
else:
  c = " + " + c
constant = c + constant

print("The quadratic equation is {} = 0".format(squaredString + xString + constant))
