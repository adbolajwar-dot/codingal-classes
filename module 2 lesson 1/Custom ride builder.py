print("====================================")
print("Welcome to the Custom Ride Builder!")
print("====================================")
print()

print("Step 1: pick your vehicle type:")
print("1. Bike")
print("2. Car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Pick your bike type:")
    print("1. Scooty")
    print("2. Mountain Bike")
    print()

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You have picked a Scooty!")
        print("Top speed is 80km/h")
        print("Best for city roads")
    else:
        print("You have picked a Mountain Bike!")
        print("Top speed is 40km/h")
        print("Best for off-road trails")

elif choice == 2:
    print("Step 2 pick your car type:")
    print("1. Sedan")
    print("2. SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You have picked a Sedan!")
        print("There are 5 seats in the car")
        print("Best for family trips")
    else:
        print("You have picked an SUV!")
        print("There are 7 seats in the car")
        print("Best for off-road adventures")

else:
    print("That was not a valid choice.")
    print("Enter 1 for bike and 2 for car.")
    print()

print("=====================================")
print("    Your Custom Ride is Ready!  ")
print("=====================================")

