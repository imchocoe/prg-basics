car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
###
# Bubble sort
#
def bubble_sort(arr):
    x=0
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                x=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=x
                


    return arr


print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

print(bank_transactions)
sortedbt=bubble_sort(bank_transactions)
print(sortedbt)