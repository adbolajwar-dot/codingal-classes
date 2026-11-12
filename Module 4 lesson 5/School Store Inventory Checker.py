# Part 1: Create the store's items names and stock counts
items = {"pencil": 20, "eraser": 15, "notebook": 25, "sharpener": 10, "glue": 30}
stock_counts = [12, 0, 8, 5, 3]

# Part 2: Pair items with stock counts into a dictionary
inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full inventory:", inventory)

# Part 3: Filter only the items that are still in stock
in_stock_items = [item for item in inventory if inventory[item] > 0]
print("Items in stock:", in_stock_items)

# Part 4: Ask the shopper which items they want to buy
chosen_item = input("Which item do you want to buy?")

# Part 5: Stop the checker early if the chosen item is out of stock
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock! Stopping the checker.")
    exit()

# Part 6: Create prices and ask for a markup amount
prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price: "))

# Part 7: Apply the markup to every price using map()
marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked up prices:", marked_up_prices)

#Part 8: Find the marked up pric of the chosen item
item_index =  list(inventory.keys()).index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("Price of", chosen_item, "after markip:", chosen_price)

# Part 9: Reduce the stock count after the purchase
inventory[chosen_item] = inventory[chosen_item] - 1
print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])

# Part 10: Print the final store summary
print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print("Item Bought:", chosen_item)
print("Price Paid:", chosen_price)
print("Updated Inventory:", inventory)
print("============================================")
