print("School Club Member Badge")

name = input("Enter your name:")
club = input("enter your club name:")

number = 8
points = 9.5
is_active = True

print("Name:", name, "-> type:", type(name))
print("Points:", points, "-> type:", type(float))
print("Club:", club, "-> type:", type(club))
print("Active:", is_active, "-> type:", type(is_active))

first_three  = name[0:3]
last_letter = club[-1:]
badge_code = first_three + last_letter
print("First 3 letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Secret Code Name:", badge_code)

print("===== CLUB BADGE =====")
print("Member:" +name)
print("Club:" +club)
print("Code:" +badge_code)
print("Points:" + points)