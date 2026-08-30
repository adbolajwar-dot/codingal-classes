print("=== ATM Cash Dispenser ===\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter Customer Name: ")
    amount = int(input(f"Hello {name}, please enter the amount you wish to withdraw: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        continue

    print(f"\nDispensing {amount} units for {name}:")
    remaining_amount = amount
    idx = 1
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining_amount // value
        if count > 0:
            print(f"  {count} x {value}-unit note(s) = {count * value} units")
            remaining_amount -= count * value
            if value == 100: total_10+= count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            else: total_1 += count
        idx += 1

        customers_served += 1
        total_dispensed += amount
        print(f"Transaction complete, {name}. Please take your cash.\n")
        again = input("Next customer? (yes/no): ").strip().lower()
        if again != "yes":
            serving = False
    print("\n=== Daily Denomination Report ===")
    for slot in range(1, 7):
        if slot == 1: value = 100; count = total_100
        elif slot == 2: value = 50; count = total_50
        elif slot == 3: value = 20; count = total_20
        elif slot == 4: value = 10; count = total_10
        elif slot == 5: value = 5; count = total_5
        else: value = 1; count = total_1
        if count > 0:
            print(f"  {value}-unit notes dispensed : {count} ", end="")
            for note in range(count):
                print("=", end="")
            print()
    print(f"\nTotal customers served: {customers_served}")
    print(f"Total amount dispensed: {total_dispensed} units")
    print("ATM session closed. GOodbye!") 