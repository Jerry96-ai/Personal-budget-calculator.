print("=== PERSONAL BUDGET CALCULATOR ===")
# Monthly income 
income = 1000
# Monthly expenses 
rent = 400
food = 150
transport = 65
other = 70  
#Monthly savings
save = 315

# caculate total expenses
total_expenses = rent + food + transport + other 

# calculate remaining money after expenses and savings
remaining = income - total_expenses - save

# Display results
print("\n--- Monthly BUDGET SUMMARY ---")
print("Monthly income: $", income)
print("rent: $", rent)
print("food: $", food)
print("transport: $", transport)
print("savings: $", save)
print("other: $", other)

print("--------------------------------")
print("Total Expenses: $", total_expenses)
print(" Money Remaining: $", remaining)