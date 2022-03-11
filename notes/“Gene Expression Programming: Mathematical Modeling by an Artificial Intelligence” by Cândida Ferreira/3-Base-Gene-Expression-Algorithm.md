# The Base Gene Expression Algorithm 

- The fundamental steeps of gene expression algorithm (GEA) are schematically represented in the following diagram: 
![img](3.1.png)

- Process begins with random generation of chromosomes of a certain number of individuals (called Initial Population)
- Then, these chromosomes are expressed, and the fitness of each individual is evaluated against a set of fitness cases (also called selection environment)
    - Fitness cases can be seen as inputs to a problem
- Individuals are selected according to fitness (their performance in that particular environment), to reproduce with modifications, leaving progeny with new traits
- This individuals will, in turn, follow the same process of expression, confrontation of environment, selection, reproduction with modifications. 
- The process is repeated for a certain number of generations, or until a good solution is found 

This chapter explores this steps in depth. The goal is to understand the logistics of GEA, but also to understand why and how populations of computer programs become better and better as they evolve. 

## Population of Individuals

- An initial population must be created in order to get things started 
- Subsequent populations are descendants via genetic modification, of this initial (or founder) population
- In GEP, it is only necessary to generate random simple chromosomal structures to get things going 
    - Random works, as any genome is valid, due to the properties we saw before
- This is a trivial task, and one of the great advantages of this technique

- Then, for each problem, we must choose the set of terminals used to create the chromosomes and the set of functions we believe to be appropriate to solve the problem. 
    - The set of terminals represents the variables and constants that the problem will use 
- We must also choose the length of each gene, the number of genes per chromosome, and how they interact with one another
- Finally, we must provide a set of fitness cases (selection environment) that will help us measure the fitness of each individual, and choose which individuals to reproduce

### Creation of Initial Population 

- Chromosomes of individuals on initial population are randomly generated using symbols representing functions and terminals chosen
    - Remember they will always be valid if we fill head with functions and terminals, and tail with just terminals
- Usually, this individuals are not very good, but they are all we need to get started, as evolution will take care of the rest
- Problem with random generation of initial population is that, sometimes, specially with small populations or fitness cases not broad enough, or tight fitness function, it might happen that none of the initial chromosomes encoded viable individuals (due to their fitness), and the run is aborted.  
