with open("../Data/rosalind_rna.txt", "r") as file:
        data = file.read().strip()

rna_sequence = data.replace("T", "U")
print(rna_sequence)
