
noproduct=int(input('Enter the number of products purchased:'))
price=int(input('Enter the product price:'))
if noproduct>2:
    amount=2*price+(noproduct-2)*(price*0.75)
print(f'Number of products: {noproduct}')
print(f'Product price: {price}')
print(f'Amount to pay: {amount}')