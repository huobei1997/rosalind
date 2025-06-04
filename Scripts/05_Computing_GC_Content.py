from Bio import SeqIO

def gc_content(dna):
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_count = len(dna)
    return (g_count + c_count) / total_count * 100  

def find_highest_gc(file):
    max_gc = -1
    max_id = ""

    for record in SeqIO.parse(file, "fasta"):
        gc = gc_content(str(record.seq))
        if gc > max_gc:
            max_gc = gc
            max_id = record.id
            
    print(max_id)
    print(f"{max_gc:.6f}")

# Call the main function with the FASTA file name
find_highest_gc("../Data/rosalind_gc.txt")
