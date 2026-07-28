# ASCII Value Checker - Complete Program


print("ASCII Value Checker")

print("=" * 40)

char = input("Enter a single character: ")

if type(char) == str and len(char) == 1:
    ascii_value = ord(char)
    print(f"\nCharacter: {char}")
    print(f"ASCII Value: {ascii_value}")

    print("\nCharacter Type: ", end="")

    if ascii_value >= 97 and ascii_value <= 122:
        print("Lowercase Letter")

    elif ascii_value >= 65 and ascii_value <= 90:
        print("Uppercase Letter")

    elif ascii_value >= 48 and ascii_value <= 57:
        print("Digit")

    elif ascii_value == 32:
        print("Space")

    else:
        print("Special Character")


else:
    print("\nError: Please enter exactly ONE character!")

    
        