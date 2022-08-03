
import random

# Food option lists by cost:
low_cost = ["McDonalds", "In & Out", "Habit"]
medium_cost = ["Sizzler", "Islands", "Red Robin"]
high_cost = ["Ruth's Kris", "Yard House", "BJ's"]

# Greeting
print("\nHello Thomas.  I will help you decide where to eat for lunch.")

# Option to quit or continue program
quit_option = input("\nEnter yes to continue and no to quit: ").lower()

while quit_option != "no":
# Do these steps as long as user did not enter "no" to quit
# Do user input validation for quit_option
  if quit_option not in ["yes", "no"]:
    print("\nThat's not a valid response.")
    quit_option = input("\nEnter yes to continue and no to quit: ").lower()

  elif quit_option  == "yes":
# Otherwise if user specified yes for quit_option do these steps
# Do user input validation, make sure input is a number (float)
    try:
      budget = float(input("\nEnter how much you would like to spend (up to $100): "))
    except:
      print("\nPlease enter a valid dollar amount between 0 and $100")
      continue

# Once confirm input is a float, format it to dollar fomat,
# & recommend random choices from lists according to budget range
    else:

      if 20 < float(budget) <= 100:
        format_budget = "{:.2f}".format(budget)
        random_high_cost = random.choice(high_cost)
        print(f"\n You entered ${format_budget} You can afford a high cost option!")
        print("\nMay I suggest " + random_high_cost+" ?")

      elif 11 < float(budget) <= 20:
        format_budget = "{:.2f}".format(budget)
        random_medium_cost = random.choice(medium_cost)
        print(f"\n You entered ${format_budget} You can afford a medium cost option.")
        print("\nMay I suggest " + random_medium_cost+" ?")

      elif 5 < float(budget) <=11:
        format_budget = "{:.2f}".format(budget)
        random_low_cost = random.choice(low_cost)
        print(f"\n You entered ${format_budget} You can afford a low cost option.")
        print("\nMay I suggest " + random_low_cost +" ?")

      elif 1 < float(budget) <=5:
        format_budget = "{:.2f}".format(budget)
        print(f"\n You entered ${format_budget} . . .")
        print("\nYou may want to get something from the vending machine.")

      elif 0 <= float(budget) <=1:
        format_budget = "{:.2f}".format(budget)
        print(f"\n You entered ${format_budget} . . .")
        print("\nFood is not an option for you . . .")

      else:
        print("\nPlease enter a valid dollar amount between 0 and $100")

    quit_option = input("\nEnter yes to continue and no to quit: ").lower()

  else:
    if quit_option == "no":
      break



