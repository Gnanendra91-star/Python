def prime_generator(n):
    # Generate prime numbers up to n
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

# Take user input
n = int(input("Enter the upper limit to generate primes: "))

# Create the generator
prime_gen = prime_generator(n)

# Print the generated prime numbers
print(f"Prime numbers up to {n}:")
for p in prime_gen:
    print(p)

output:
Enter the upper limit to generate primes: 15
Prime numbers up to 15:
2
3
5
7
11
13
