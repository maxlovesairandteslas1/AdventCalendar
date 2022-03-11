# Advent Calendar
# Question no.1
# By Max Yang
# Github: Maxlovesairandteslas1

counter = 0
increased = 0
for i in range (2000):
    x = input()
    x = x.strip(" ")
    y = x[counter]
    counter = counter + 1
    z = x[counter]
    if z > y:
        increased = increased + 1


print(increased)
