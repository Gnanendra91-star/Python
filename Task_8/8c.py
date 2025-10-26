def log_prime(func):
    def wrapper(n):
        for prime in func(n):
            print(f"Prime generated: {prime}")  # log each prime
            yield prime
    return wrapper

@log_prime
def prime_generator(n):
    for num in range(2, n+1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            yield num

# Generate primes up to 20
for p in prime_generator(20):
    pass

output:
Prime generated: 2
Prime generated: 3
Prime generated: 5
Prime generated: 7
Prime generated: 11
Prime generated: 13
Prime generated: 17
Prime generated: 19
