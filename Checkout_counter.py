userProducts = []
userProductsCost = []


print("Welcome to the checkout counter! How many items are you purchasing today?")
userAmountOfProducts = int(input())

for i in range(userAmountOfProducts):
    print("Please enter the name of product " + str(i+1))
    newProduct = input()
    userProducts.append(newProduct)
    print("And how much does", newProduct, "cost")
    userProductsCost.append(float(input()))
    
print("Your order was: ")
for product, cost in zip(userProducts, userProductsCost):
    print(f"    {product} ${cost:.2f}")

subtotal = sum(userProductsCost)
taxRate = 0.09
tax = subtotal * taxRate
total = subtotal + tax


print("Your subtotal comes to", subtotal, ". With 9% sales tax, your total is", round(total, 2), "." "\nPlease enter cash amount")
userCash = float(input())
print("I owe you back", float(userCash - round(total, 2)), "\nThank you for shopping with us!")
