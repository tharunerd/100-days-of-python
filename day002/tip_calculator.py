# a simple program to split bills between friends
# It takes the total bill amount, % of tip and number of friends,
# then calculates how much each person should pay.

print("Welcome to the bill splitter")
bill = input("enter the total bill amount $")
tip = input("how much would you like to tip? 10, 12 or 15? ")
friends = input("how many friends to split the bill? ")
total_bill = float(bill) * (1 + int(tip) / 100)
each_person = total_bill / int(friends)
print("Each person should pay: ${:.2f}".format(each_person))