# Part 1 Create two fruit baskets as sets
basket1 = {"apple", "banana", "mango", "apple", "grape"}
basket2 = {"mango", "kiwi", "banana", "kiwi"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

# Part 2 add a new fruit to basket1
basket1.add("orange")
print("Basket 1 after adding orange:", basket1)

# Part 3 find the common fruits in both baskets
common_fruits = basket1.intersection(basket2)
print("Fruits in both baskets:", common_fruits)

# Part 4 create an array of fruit counts using the array module
import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts array:", fruit_counts)

# Part 5 add new fruit counts to the array
fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit counts after adding items:", fruit_counts)

# Part 6 count how many times number 4 appears in the array
count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears:", count_of_4)

#Part 7 reverse the order of the fruit counts array
fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)

# Part 8 print the final class fruit basket organizer summary
print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Shared fruits:", common_fruits)
print("Fruit counts:", fruit_counts)
print("=========================================")

