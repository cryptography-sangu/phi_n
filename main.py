import math
# Given prime numbers
p = 61
q = 53
# Calculate n and φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)
print(f"n = {n}")
print(f"φ(n) = {phi_n}")
# Function to check if a number is a valid e
def is_valid_e(e, phi_n):
    return 1 < e < phi_n and math.gcd(e, phi_n) == 1


# Find all valid e values
valid_e_values = [e for e in range(2, phi_n) if is_valid_e(e, phi_n)]

print(f"\nAll valids: {valid_e_values}")
print(f"\nNumber of valid e values: {len(valid_e_values)}")
print("First 10 valid e values:", valid_e_values[:10])
print("Last 10 valid e values:", valid_e_values[-10:])


# Check common e values
common_e_values = [3, 17, 65537]
for e in common_e_values:
    if e in valid_e_values:
        print(f"\n{e} is a valid choice for e")
    else:
        print(f"\n{e} is not a valid choice for e")


# Find the smallest and largest valid e
smallest_e = min(valid_e_values)
largest_e = max(valid_e_values)


print(f"\nSmallest valid e: {smallest_e}")
print(f"Largest valid e: {largest_e}")