###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print('5. Check pin')

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        print(f'Your pin is {pin}')
        pinchoice=input('Do you want to change your pin? (Y/N):')
        if pinchoice=="Y":
            pinn=input('Your new pin:')
            if len(pinn)==4 and pinn.isdigit():
                pin==pinn
            else:
                print('Your pin has to be 4 NUMBERS long')
        elif pinchoice=="N":
            print('Going back to menu')
        
    
    
    
    
    else:
        print("Invalid option. Please try again.")
