print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? ")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
people_amount = input("How many people to split the bill? ")
tip_amount = (int(tip_percentage)/100)+1
payment_amount = round((float(total_bill)*tip_amount)/int(people_amount), 2)
print(f"Each person should pay: {payment_amount} ")

