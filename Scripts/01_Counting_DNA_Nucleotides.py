with open("../Data/rosalind_dna.txt", "r") as file:
    data = file.read()

count = {char: data.count(char) for char in ['A', 'C', 'G', 'T']}
for char in ['A', 'C', 'G', 'T']: 
    print(count[char])

