print("=== ATM CASH DISPENSSER ===\n") 
total_100 = total_50 = total_20 = total_10 = total_5  = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter custemer name: ")
    amount = int((f"Hello {name}! Enter withdrawl amount:"))
    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        continue
    print(f"\nDispenseing {amount} units for {name}:")
    remaining = amount
    idx = 1
    while idx <= 6:
            if idx == 1: value = 100
            elif idx == 2: value = 50
            elif idx == 3: value = 20
            elif idx == 4: value = 10
            elif idx == 5: value = 5
            else: value = 1
            count = remaining // value
            if count > 0:
                 print(f"{count} x {value}-unit note(s) = {count * value} units")
                 remaining -= count * value
                 if idx == 1: total_100 += count
                 elif idx == 2: total_50 += count
                 elif idx == 3: total_20 += count
                 elif idx == 4: total_10 += count
                 elif idx == 5: total_5 += count
                 else: total_1 += count
            idx += 1
    customers_served += 1
    total_dispensed += amount
    print(f"Transaction complete, {name}!\n")
    again = input("Next customer? (yes/no): ").strip().lower()
    if again != 'yes':
        serving = False

print("\n=== Daily Denomination Report ===")
for slot in range(1, 7):
    if slot == 1: value = 100; count = total_100
    elif slot == 2: value = 50; count = total_50
    elif slot == 3: value = 20; count = total_20
    elif slot == 4: value = 10; count = total_10
    elif slot == 5: value = 5; count = total_5
    else: value, total = 1, total_1
    if total > 0:
         print(f" {value}-unit notes dispensed : {total} ", ends="")
         for note in range(total):
                print("=", end="")
    print()
    
print(f"\nCustomeers served : {customers_served}")
print(f"Total amount dispensed : {total_dispensed} units")
print("ATM session closed. goodbye!")