print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print(f"Sequence: {current_number}", end=" ")

while current_number != 1:
    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = 3 * current_number + 1
    step_count += 1
    print(current_number, end=" ")
print()
print(f"Steps: {step_count}")
print()

print("=== Challenge 2: Prime Number Checker ===")
number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {number-1}...")

is_prime = True

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        is_prime = False
        break

if is_prime:
    print(f"{number} is prime!")
print("")


