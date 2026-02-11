# Asks the meal price
meal_price = float(input("What is the meal price?")) 

if meal_price <=0:
  print("Invalid meal price.")
  exit()

# Asks the tip price
tip_price = float(input("How much will you tip?"))
if tip_price < 0:
  print("Positive numbers only.")

# Calculates the tip
tip_percent = tip_price / 100 * meal_price

# Calculates the total of the entire meal + tip
meal_total = round((meal_price + tip_percent), 2)

print(f"Your total is: {str(meal_total)}.")
