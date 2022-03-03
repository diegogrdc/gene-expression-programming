# Notes on “Gene Expression Programming: Mathematical Modeling by an Artificial Intelligence” by Cândida Ferreira


## Introduction : The Biological Perspective

This chapter goes through the differences of Gene Expression Programming (GEP) to its predecessors, Genetic Algorithms (GAs) and Genetic Programming (GP). 

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
