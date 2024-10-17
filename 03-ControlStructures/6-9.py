age=int(input("Enter the dog's age in human years:"))
if age==1:
    print("The dog's age in dog years is 10.5")
elif age==2:
    print("The dogs age in dog years is 21")
else:
    dogage=21+(age-2)*4
    print(f"The dog's age in dog years is:{dogage}")

