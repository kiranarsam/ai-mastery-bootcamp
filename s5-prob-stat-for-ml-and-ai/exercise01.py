from itertools import product

# Sample space of a dice roll
sample_space = list(range(1, 7))
print("sample space list: ", sample_space)

# Probability of rolling an even number
even_numbers = [2, 4, 6]
p_even = len(even_numbers) / len(sample_space)

print("P(Even): ", p_even)
