# Introduction : The Biological Perspective

The aim of the chapter is to bring focus on the basic differences of Gene Expression Programming (GEP) to its predecessors, Genetic Algorithms (GAs) and Genetic Programming (GP). 

- All these algorithms use a population of individuals, select through fitness, and do genetic variation. 
- The difference resides on the nature of individuals 
    - GAs -> Symbolic strings of fixed length (chromosomes)
    - GP -> nonlinear entities of different sizes and shapes (parse trees)
    - GEP -> nonlinear entities of different sizes and shapes (expression trees), encoded as simple string of fixed length (chromosomes)

- Difference between GAs and GP is superficial, as both use one entity that works as both genotype and body (phenotype)
    - This brings up limitations
    - They can be easy to manipulate genetically, but this makes them lose functional complexity (as in GAs)
    - If they are funcionally complex, they are extremely hard to reproduce with modifications (as in GP)

- In GEP, chromosomes/expression trees and expressions are always valid. Invalid expressions do not exist. 
- This makes GEP a simple artifficial system, well established beyond the replicator threshold, that other algorithms struggle with. 

To understand the fundamental differences, and to really get why GEP is such a leap forward over other algorithms, the book gives a bit of information on the main players of biological gene expression and how they work togheter

- Cell has a few important main players for our purpose of understanding: DNA, RNA and Proteins. 
    - DNA is the carrier of genetic information
    - Proteins read and express that information
    - RNA is a working copy of DNA. Its existence makes sense on the real world, but in computer systems like GEP is of little use

To go a bit deeper

### DNA
- Long, linear strings of nucleotides (A, T, C, G)
- Sequence consists of genetic information 
- Double helix, and each string is complementary of the other (does not add any info) 
- Each nucleotie matchs with another. A with T and C with G. 
- Double stranded model is helpful in nature, but not in GEP or GAs which use single stranded DNA
- Excelent to store information
- Incapable of both catalytic activity and structural diversity
    - This means the potencial functional groups (ATCG) are locked up in the helix
    - Molecule lacks tertiary structure, a requisite for this actions

### RNA

- Eorking copy of a particular sequence of DNA (contains same info)
- Role in information decoding
- Long linear strings with nucleotides (A U C G) and single stranded
- Can have a tertiary structure that gives them some degree of structural and functional diversity 
- Can function as ribozymes (catalysts)
- Can function as genotype and phenotype simultaneously
    - Both are tied up togheter. Any modification to one directly affects the other
    - This means no room for subtle or neutral changes, which can affect efficient evolution

### Proteins 

- Linear, long strings of 20 different aminoacids
- Consist of immediate expression of genetic information stored in DNA
    - 4-letter language in DNA is translated into 20-letter languange of proteins
- Triplets of nucleotides for each aminoacid (codons)
    - This gives 64 possible combinations
    - Some amino acids have multiple codons
- Unique 3D structure allows them to take role of catalysts or enzymes
- Can function simultaneously as genotype and phenotype but equally constrained as both are tied 

About information store in DNA, gene coding for proteins is relevant to us and a bit of context on biological gene expression and how it changes over time

 - Nature's diversity is largely a consequence of the effects of restructuring processes that take place on the genomes of organisms
     - This creates a diversity of protein functions

 - When a genome replicates itself and passes genetic information to the next generation, the sequence of the daughter molecule sometimes differ from the mother in one or more points
     - This is due to mismatched nucleotides that are not fixed
- In a gene, the replacement of a nucleotide can have different effects
    - New codon might code for a new amino acid (missense mutation)
    - new codon might code for a stop codon, truncating the protein (nonsense mutation)
    - a stop codon is lost, which elongatees the chain (nonsense mutation)
    - Point mutations, where codon represents same amino acid (neutral mutation)
- In other kinds of mutation, large or small fragments may be inserted or deleted in a gene, which usually create a defective protein
- The effects caused can be quite different  
    - Effects may be neutral, not changing anything
    - Changing slightly the protein function, which might occasionally improve efficency of the protein
    - Effects can be lethal, specially on fundamental proteins
    - Occasionaly, mutations might give rise to new revolutionary traits
- Recombination happens when some fragments of genetic material are exchanged between two distinct donor molecules, so offspring contains genetic information from both
    - Two chromosomes are paired and exchange some material between them, forming two new daughters chromosomes
- Transposition represents when genes that can move from place to place within the genome
    - They can inactivate genes, activate adjacent genes, or even activate a recombination
    - Very occcasionaly, it might create a new protein
- Gene duplication happens when a gene is copied twice
    - This might cause protein to evolve into a different one 

The expression of genetic information uses an intermediate molecule called messemger RNA (mRNA), and the process of its synthesis is called transcription 
- During transcription, sequence of a gene is copied into an mRNA
- This has all instructions to start stop and to synthesize the protein
- This makes sense on the cell, but is of no use on computers

- After translation, proteins can have posttranslational modifications
- Each level of protein organization is built on lower levels, an everything is dictated by the primary structure of the protein
- When a protein folds itslef, amino acids really far might be brought togheter, or neighbor amino acids might face different ways, thus being involved in distinct aspects of the structure and functionalities

Much of the diversity we see in the living world, results from the accumulation of mutations in proteins. The modifications that occur at the molecular level in proteins enable populations of organisms to develop new abilities, adapt to environments and ultimately become new species. 
For populations to adapt in the long run, individual organisims must reproduce, and the survival of an organism is important only if it leaves progeny, because they can exhibit new traits and adapt better. The better adapted leave more offspring. 

## GAs, GP, GEP

- GA was invented by John Holland in the 60s as an oversimplification of biological evolution (GAs)
    - GAs individuals consist of chromosomes (0 and 1), simple replicators tht work both as genotype and phenotype. 
    - GAs are simple but very limited, as the genotype is tied to phenotype, and due to its simple structure
- GP was invented on 1985 and developed on 1992. 
    - Nonlinear structures or parse trees with different sizes and shapes
    - More varied alphabet, but lack of autonomous genome
    - Great variety of functionalities, but reproduction is constrained due to its complex structure
    - Really hard to keep all options valid
    - Limited mutation operators don't bring a lot new on generations
    -
- GEP was invented by the author of this book in 1999
    - Incorporates both simple chromosomes and ramified structures of different shapes, which are encoded on the chromosome. 
    - In GEP the genotype and phenotype are finally separated from one another (!!!) 
    - This means system can benefit from evolutionary advantages this brings
    - This is all thanks to the invention of a chromosome capable of representing any parse tree
    - Karva language was invented to reead and express information encoded in the chromosomes
    - Allows the creation of multiple genes, each coding for smaller program or sub expression tree
    - Only genetic algorithm with multiple genes
    - Versatile structure that allows to implement very powerful set of genetic operations that can efficiently search the solution space
    - Always generates valid structures  
