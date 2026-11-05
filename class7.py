print("=======================================")
print("       Welcome to ride builder         ")
print("=======================================")
print()

print("Step 1: Pick your vehicle")
print(" 1 - Bike")
print(" 2 - Car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    #Nested if-else - runs only when choice is 1
    print(" 1 - Scooty")
    print(" 2 - mountain bike")
    print()
    
    bike_type = int(input("Enter 1 or 2: "))

    if bike_type == 1:
        print("You picked  : Scooty")
        print("Top speed   : 80 km/h")
        print("Best for    : City rides")
    else:
        print("You picked  : Mountain Bike")
        print("Top speed   : 40 km/h")
        print("Best for    : Off-road trails")
elif choice == 2:
    print("step 2: Pick your car type")
    print(" 1 - Sedan")
    print(" 2 - SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))

    if car_type == 1:
        print("You picked  : Sedan")
        print("seat        : 5 passengers")
        print("Best for    : family trips")
    else:
        print("You picked  : SUV")
        print("seats       : 7 passengers")
        print("Best for    : Off-road adventures")
else:
    print("That was not a valid choice.")
    print("Please enter 1 for bike and 2 for Car")


print()
print("=======================================")
print("       your custom ride is ready!      ")
print("       Enjoy the journey!              ")
print("=======================================")