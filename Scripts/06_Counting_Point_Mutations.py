with open("../Data/rosalind_hamm.txt") as file:
    s, t = [line.strip() for line in file.readlines()]

def hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length.")
    
    # Calculate the number of differing characters
    distance = sum(el1 != el2 for el1, el2 in zip(s, t))
    return distance

distance = hamming_distance(s, t)
print(distance)  
