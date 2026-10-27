#part 1: ask for today's tempreture

temperature = int(input("Enter today's temperature in Celsius: "))

#part 2:decide between a jacket and a t-shirt
if temperature < 20:
    outfit = "Jacket"
    print('it is cold today')
    print("wear a", outfit)
else:
    outfit = "T-shirt"
    print('it is warm today')
    print("wear a", outfit)

#part 3: ask whether it is raining
is_raining = input("IS it raining today? (yesy/no):")

#part 4: decide whether to bring an umbrella
if is_raining == "yes":
    print("bring an umbrella")

#part 5: ask for the wind speed
wind_speed = int(input("Enter today's wind speed in km/h: "))

#part 6: decide whether to bring a windbreaker
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy")
    print("wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("It is calm today.")
    print("No windbreaker needed over yout", outfit)

#part 7: ask whether there are puddles on the ground
has_puddles = input("are there puddles on the ground? (yes/no)")

#part 8:decide between boots and sneakers
if has_puddles == "yes":
    shoes = "boots"
    print("the ground is wet")
    print("wear", shoes)
else:
    shoes = "sneakers"
    print("the ground is dry")
    print("wear", shoes)

#part 9: this message always prints, no matter what was chosen above
print("")
print("Weather check complete")

#part 10: print the final outfit summary
print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("shoes chosen:", shoes)
print("====================================")