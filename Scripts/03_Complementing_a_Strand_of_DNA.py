with open("../Data/rosalind_revc.txt") as file:
    dna = file.read().strip()

# Function to compute the reverse complement
def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented = ''.join(complement[nuc] for nuc in reversed(dna))
    return complemented

sc = reverse_complement(dna)
print(sc)
