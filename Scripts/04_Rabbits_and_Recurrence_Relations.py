with open("../Data/rosalind_fib.txt") as file:
    n, k = map(int, file.readline().strip().split())

# Function to compute the number of rabbit pairs
def wabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, curr + k * prev
        return curr

# Calculate the total pairs of rabbits
total_pairs = wabbits(n, k)
print(total_pairs)
