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

a = str(input("Enter the first coefficient: "))
b = str(input("Enter the second coefficient: "))
c = str(input("Enter the third coefficient: "))

squaredString = "x^2"
xString = "x"
constant = ""
stringFinal = ""


if (abs(int(a)) != int(a)):
  if (abs(int(a)) == 1):
    squaredString = "- " + squaredString
  else:
    squaredString = "- " + a[1:] + squaredString
if int(a) == 0:
  squaredString = ""

if int(b) == 0:
  b = ""
  xString = ""
elif abs(int(b)) == 1:
  if abs(int(b)) != int(b):
    b = " - "
  else:
    b = ""
elif abs(int(b)) != int(b):
  b = " - " + b[1:]
else:
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

print(squaredString + xString + constant)
