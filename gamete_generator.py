genotype = input("Enter genotype: ")
number_of_genes = len(genotype) // 2
print("Number of genes:", number_of_genes)

genes = []
for i in range(0,len(genotype),2):
    gene = genotype[i:i+2]
    genes.append(gene)
print(genes)
allele_options = []
for gene in genes:
    if gene[0] == gene[1]:
        allele_options.append([gene[0]])
    else:
        allele_options.append([gene[0], gene[1]])
print("Alleles:" , allele_options)

number_of_gametes = 1
for alleles in allele_options:
    number_of_gametes = number_of_gametes * (len(alleles))
print("Number of possible gametes:" , number_of_gametes)

gametes = [""]

for alleles in allele_options:
    new_gametes = []
    for gamete in gametes:
        for allele in alleles:
            new_gametes.append(gamete + allele)
    gametes = new_gametes
print("possible gametes:",gametes)
