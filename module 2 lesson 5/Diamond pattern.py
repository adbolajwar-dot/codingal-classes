n = int(input("Enter the number of rows: "))

for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()