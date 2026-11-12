total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Do the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! chore completed.")
    else:
        print("Okay, finish it and check agian!")

    print("Chores remaining:", total_chores - completed_count)
    print()



print("==========ALL CHORES COMPLETE!=========")
print("great work finishing all your chores!")

print("Now lets safely peek at an infinite loop...")
test_value = 0
saftey_counter = 0
while test_value < 5:
    print("This condition never changes, so this would run forever!")
    saftey_counter += 1
    if saftey_counter == 100:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break


print("\n===== Chore Completion Summary =====")
print(f"Total chores assigned: {original_count}")
print(f"Total chores completed: {completed_count}")
print(f"Total chores remaining: {original_count - completed_count}")
print("======================================")