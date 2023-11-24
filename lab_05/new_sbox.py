from itertools import permutations

# Define the set of values
values_set = set(range(32))

# Generate 16 lists with permutations
lists = [list(perm) for perm in permutations(values_set, 32)]

# Take the first 16 unique lists
unique_lists = lists[:16]

# Display the 16 lists
for i, lst in enumerate(unique_lists):
    print(f"List {i + 1}: {lst}")
