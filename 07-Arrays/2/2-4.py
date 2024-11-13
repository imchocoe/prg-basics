# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   plan=""
   if day_number==1:
      plan=meal_plan[0][0:]
   elif day_number==2:
      plan=meal_plan[1][0:]
   elif day_number==3:
      plan=meal_plan[2][0:]
   elif day_number==4:
      plan=meal_plan[3][0:]
   elif day_number==5:
      plan=meal_plan[4][0:]
   elif day_number==6:
      plan=meal_plan[5][0:]
   elif day_number==7:
      plan=meal_plan[6][0:]
   return plan


print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
print(weekday(1))
print(day_meal_plan(meal_plan,1))
print(weekday(2))
print(day_meal_plan(meal_plan,2))
print(weekday(3))
print(day_meal_plan(meal_plan,3))
print(weekday(4))
print(day_meal_plan(meal_plan,4))
print(weekday(5))
print(day_meal_plan(meal_plan,5))
print(weekday(6))
print(day_meal_plan(meal_plan,6))
print(weekday(7))
print(day_meal_plan(meal_plan,7))