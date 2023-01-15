print("Welcome to the tipp calculator")

bill = int(input("What was the total  bill? $"))

percentage = int(input("What percentage would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

amount = round(((bill * ((100 + percentage)/100))/ people), 2)

print(f"Each person should pay ${amount}")
