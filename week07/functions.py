# AI USE: Explainer (asked about IndexError on line 105)
# The first bug I spotted was the IndexError. I found it by explaining the code out loud and realized that the code was trying to access a list position that did not exist. I learned that I need to pay attention to error messages and check where my loop stops.
# The function takes a price and a tier and applies a discount based on the tier, then returns the new price. A colleague could use it by looking at the name of the function and inputs to understand what it does.
# The AI use helped me understand the error and why it was happening, which helped me understand how to fix it myself.

# Exercise 1 

# Define calculate tax function 

def calculate_tax(price, rate): 
    return price * rate 

# Calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on 250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2 

def apply_discount(price, teir):
    if teir == "gold":
        return price * 0.85  # 20% discount
    elif teir == "silver":
        return price * 0.90  # 10% discount
    elif teir == "bronze":
        return price * 0.95  # 5% discount
    else:
        return price  

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers: 
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3 

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}") 
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders: 
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final Price: ${total:.2f}")

# Exercise 6 

x=100 # apple # Global

def double_it(): 
    x=999 # another apple (not the same as the first apple)
    return x * 2

print(x) 
print(double_it())
print(x)

# Scope is where a variable can be used in the code.
# The output is 100, 1998, and 100 because the global x begins at 100. The function uses a local x of 99 and doubles it to get 1998. The global x stays 100 because the local variable does not change it.

# Exercise 5 
# broken_sales.py - trace and diagnose before fixing anything.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
    print(f"Current sale: {sale}, Total: {total}")

print(f"Final total: {total}")

count = 0
for sale in sales:
    count += 1
    print(f"Current count: {count}")

print(f"Total sales: {count}")

i = 0
# I changed <= to < because the list starts at index 0, so the last index is 4, not 5. This stops the error.
while i < len(sales):
    print(f"Index: {i}")
    print(sales[i])
    i += 1
