# intering the integer
n = int(input("Enter a positive non-zero integer: "))

print("The divisors of",n,"are:")

# Loop through all possible divisors
for i in range(1, n + 1):
    if n % i == 0:  # If i is a divisor of n
        print(i)
