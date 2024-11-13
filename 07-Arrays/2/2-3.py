# Weekly expenses for different categories
# [Food, Transport, Utilities]
#total expenses for each category
#total expenses for each week
#total expenses for a month
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
#weeks
a1=max(monthly_expenses[0])
a2=max(monthly_expenses[1])
a3=max(monthly_expenses[2])
a4=max(monthly_expenses[3])

#categories
food=0
transport=0
utilities=0

for f in range(0,4):
    food+=monthly_expenses[f][0]
for t in range(0,4):
    transport+=monthly_expenses[t][1]
for u in range(0,4):
    utilities+=monthly_expenses[u][2]


total=food+transport+utilities


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',a1)
print('Week 2:',a2)
print('Week 3:',a3)
print('Week 4:',a4)
print('---------------')
print('TOTAL:',total)