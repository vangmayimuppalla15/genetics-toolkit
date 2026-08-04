genotype = input("Enter genotype: ")
number_of_genes = len(genotype) // 2
print("Number of genes:", number_of_genes)

for i in range(0, len(genotype), 2):
    gene = genotype[i:i+2]
    print(gene)