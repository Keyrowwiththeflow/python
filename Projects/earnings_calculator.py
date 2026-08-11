# This program will ask the user how much money they want to save in a year.
earningsgoal = int(input("Write how much money you want to save this year:"))
months = earningsgoal / 12
weeks = earningsgoal / 4
days = earningsgoal / 365
print("To save " + str(earningsgoal) + " dollars per year, you will need to save " + str(round(months, 2)) + " dollars per month.")
print("To save " + str(earningsgoal) + " dollars per year, you will need to save " + str(round(weeks, 2)) + " dollars per week.")
print("To save " + str(earningsgoal) + " dollars per year, you will need to save " + str(round(days, 2)) + " dollars per day.")