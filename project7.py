print("What holiday are you celebrating next?")
print("1 - halloween")
print("2 - Diwali")
print("3 - Christmas")
holiday = int(input("Enter 1, 2 or 3: "))

if holiday == 1:
    print("you picked halloween!")
    print("pick your costume:")
    print("1 - witch")
    print("2 - vampire")
    costume = int(input("Enter 1 or 2: "))
    if costume == 1:
        print("you picked witch!")
        print("you will need a broomstick and a black hat")
        print("you will need a black dress and black shoes")
        print("this costume will be spooky")
    elif costume == 2:
        print("you picked vampire!")
        print("you will need a cape and fangs")
        print("you will need a black suit and black shoes")
        print("this costume will be scary")
elif holiday == 2:
    print("You picked diwali!")
    print("Pick your firework:")
    print("1 - sparklers")
    print("2 - rockets")
    firework = int(input("Enter 1 or 2: "))
    if firework == 1:
        print("you picked sparklers!")
        print("you will need a lighter and a sparkler")
        print("you will need to light the sparkler in a safe place")
        print("this firework will be fun")
    elif firework == 2:
        print("you picked rockets!")
        print("you will need a lighter and a rocket")
        print("you will need to light the rocket in a safe place")
        print("this firework will be exciting")
elif holiday == 3:
    print("You picked christmas!")
    print("Pick your decoration:")
    print("1 - christmas tree")
    print("2 - christmas lights")
    decoration = int(input("Enter 1 or 2: "))
    if decoration == 1:
        print("you picked christmas tree!")
        print("you will need a tree and ornaments")
        print("you will need to decorate the tree with lights and ornaments")
        print("this decoration will be festive")
    elif decoration == 2:
        print("you picked christmas lights!")
        print("you will need lights and extension cords")
        print("you will need to hang the lights on your house or tree")
        print("this decoration will be bright and cheerful")
else:
    print("Invalid input. Please enter 1, 2 or 3.")