#WAP to calculate the selling price of book based on cost price and discount

cost_price=float(input("Enter the cost_price :"))
discount_price=float(input("Enter the discount_price :"))

discount_price=(cost_price*discount_price)/100
selling_price=(discount_price-cost_price)
print("selling price is :",selling_price)