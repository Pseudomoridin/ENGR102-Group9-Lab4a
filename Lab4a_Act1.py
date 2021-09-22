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

ticket = float(input("Enter Ticket: "))
lost_ticket = False
price = 0
rate = -1
if (abs(ticket) != ticket):
  price += 36
  ticket = abs(ticket)
if (ticket // 1 != ticket):
  ticket = int((ticket // 1) + 1)

days = int(ticket // 24)
ticket = ticket % 24

for x in range(days):
  price +=  24

# Price per individual hour
if (ticket > 0):
  if ticket > 2:
    price += 4 * 2
  else:
    price += 4 * ticket
  ticket -= 2
if (ticket > 0):
  if ticket > 2:
    price += 3 * 2
  else:
    price += 3 * ticket
  ticket -= 2
if (ticket > 0):
  price += ticket * 1

print("${:.2f}".format(price))
