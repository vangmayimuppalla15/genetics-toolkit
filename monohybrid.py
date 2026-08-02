parent1 = input("enter parent 1 genotype:") #INPUT
parent2 = input("enter parent 2 genotype:")

print ("alleles of parent 1:") #SHOW ALLELES OF PARENT 1

print (parent1[0])
print (parent1[1])

print("alleles of parent 2:")  #SHOW ALLELES OF PARENT 2

print (parent2[0])
print (parent2[1])

print ("the recombination of two alleles is:") #GENERATE COMBINATIONS

offspring1 = (parent1[0] + parent2[0])
offspring2 = (parent1[0] + parent2[1])
offspring3 = (parent1[1] + parent2[0])
offspring4 = (parent1[1] + parent2[1])
                                       #FIX GENOTYPE NOTATION
if offspring1[0].islower() and offspring1[1].isupper() :
    offspring1 = offspring1[1] + offspring1[0]
if offspring2[0].islower() and offspring2[1].isupper() :
    offspring2 = offspring2[1] + offspring2[0]
if offspring3[0].islower() and offspring3[1].isupper() :
    offspring3 = offspring3[1] + offspring3[0]
if offspring4[0].islower() and offspring4[1].isupper() :
    offspring4 = offspring4 [1] + offspring4[0]

print("offspring1:" , offspring1)
print("offspring2:" , offspring2)
print("offspring3:" , offspring3)
print("offspring4:" , offspring4)


print("THE PUNNET SQUARE:")

print("  " ,"| " ,parent2 [0] ," | " ,parent2 [1])
print("---+-----+------")
print(parent1[0] , " | ",offspring1 , "| " ,offspring2)
print("---+-----+------")
print(parent1[1] , " | ", offspring3 , "| " ,offspring4)

TT_count = 0        #GENOTYE RATIO
Tt_count = 0
tt_count = 0

if offspring1 == "tt":
    tt_count = tt_count + 1
if offspring1 == "Tt":
    Tt_count = Tt_count + 1
if offspring1 == "TT":
    TT_count = TT_count + 1

if offspring2 == "TT":
    TT_count = TT_count + 1
if offspring2 == "Tt":
    Tt_count = Tt_count + 1
if offspring2 == "tt":
    tt_count = tt_count + 1

if offspring3 == "Tt":
    Tt_count = Tt_count + 1
if offspring3 == "TT":
    TT_count = TT_count + 1
if offspring3 == "tt":
    tt_count = tt_count + 1

if offspring4 == "TT":
    TT_count = TT_count + 1
if offspring4 == "Tt":
    Tt_count = Tt_count + 1
if offspring4 == "tt":
    tt_count = tt_count + 1 

print ("GENOTYPE RATIO:")
print("TT:", TT_count)
print("Tt:", Tt_count)
print("tt:", tt_count)

dominant_count = 0                      #PHENOTYPE RATIO
recessive_count = 0

if offspring1[0].isupper() or offspring1[1].isupper():
    dominant_count = dominant_count + 1
else: recessive_count = recessive_count + 1

if offspring2[0].isupper() or offspring2[1].isupper():
    dominant_count = dominant_count + 1
else: recessive_count = recessive_count + 1

if offspring3[0].isupper() or offspring3[1].isupper():
    dominant_count = dominant_count + 1
else: recessive_count = recessive_count + 1

if offspring4[0].isupper() or offspring4[1].isupper():
    dominant_count = dominant_count + 1
else: recessive_count = recessive_count + 1

print ("PHENOTYPE RATIO:")
print("Dominant:", dominant_count)
print("Recessive:", recessive_count)



