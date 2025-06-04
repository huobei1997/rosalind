def dominant_allele_probability(k, m, n):
    total_population = k + m + n
    
    # Calculate the probabilities of each mating combination
    p_kk = (k / total_population) * ((k - 1) / (total_population - 1))  
    p_kk_m = (k / total_population) * (m / (total_population - 1)) + (m / total_population) * (k / (total_population - 1))  
    p_kk_n = (k / total_population) * (n / (total_population - 1)) + (n / total_population) * (k / (total_population - 1))  
    p_mk = (m / total_population) * ((m - 1) / (total_population - 1))  
    p_mn = (m / total_population) * (n / (total_population - 1)) + (n / total_population) * (m / (total_population - 1))  
    
    # Calculate probabilities of producing a dominant phenotype
    probability_dominant = (p_kk + p_kk_m + 
                             p_mk * 0.75 + 
                             p_kk_n + 
                             p_mn * 0.5)
    
    return probability_dominant

# Example usage
k = 21  # Homozygous dominant
m = 15  # Heterozygous
n = 15  # Homozygous recessive

result = dominant_allele_probability(k, m, n)
print(result)
