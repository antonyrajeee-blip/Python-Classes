n = int(input("Enter the number whose sum you want to find: "))
sum = 0

for i in range(1, n+1):
    sum = sum+1
    print("\nSum =", sum)


#reverse a string
string = input("Enter a string to reverse: ")

string2 = ('')
for i in string:
    string2 = i + string2

print("\nThe Original String = ", string)
print("The Reversed String = ", string2) 

#Reverse order
n = int(input("Enter the value of n:  "))

print("number from {0} to {1} are: ".format(n,1))

for i in range(n,0,-1):
    print(i)