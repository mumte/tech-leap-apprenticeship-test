data = [
  {"item": "Pen", "price": 20, "quantity": 3},
  {"item": "Book", "price": 200, "quantity": 2},
  {"item": "Bag", "price": 800, "quantity": 1}
]

def total_revenue(sales_data):
    """
    This function calculates total revenue
    by multiplying price * quantity for each item.
    """
    total = 0
    for record in sales_data:
        total += record["price"] * record["quantity"]
    return total

print("Total Revenue:", total_revenue(data))

# Explanation:
# I loop through each item in the list, multiply its price by quantity,
# and sum up all the results to get total sales revenue.
