while True:
 try:       
    # Asks the meal price
    meal_price = float(input("What is the meal price?")) 

    if meal_price > 0:
         break
    else:  
        print("Invalid meal price.")
        
 except ValueError:
        print("Input only numbers.")


# Asks the tip price
while True:
  try:
    tip_price = float(input("How much percent will you tip?"))
    if tip_price > 0:
        break
    else:
      print("Positive numbers only.")
  except ValueError:
      print("Input only numbers.")

# Calculates the tip
tip_percent = tip_price / 100 * meal_price

# Calculates the total of the entire meal + tip
meal_total = round((meal_price + tip_percent), 2)

print(f"Your total is: {str(meal_total)}.")
