# The Base Gene Expression Algorithm 

- The fundamental steeps of gene expression algorithm (GEA) are schematically represented in the following diagram: 

<p align="center"><img src="./img/3.1.png" width="300"/></p>

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
- To avoid this issue, we can introduce a start up control. 
    - This control is set by default to one viable individual
    - This does not hinder the evolutionary process, as GEP populations can evolve efficiently even with just one viable founder  
    - This control, with cloning of best individual prevents the existence of failed runs in GEP
- If all individuals of initial population happens to have zero fitness, another initial population is randomly generated, until at least one viable individual is created and evolutionary process can resume

### Subsequent Generations and Elitism

- From generation to generation, the best individual (or one of the best) is replicated unchanged into the next generation. 
    - If more than one have the same best fitness, the last one is chosen to become a clone
- The cloning the best (simple elitism), guarantees that at least one descendant will be viable (in problems where selection environment is the same in all generations)
- Elitism has a big advantage on high modification rates, as we don't have the risk of causing a mass extinction
- In GEP, populations are always evolving at high creative rates in creative periods 
    - AI gives the opportunity to have much faster evolution and in constant turmoil, allowing the discovery of good solutions in record time
    - This is in really different in nature, as adaptation and evolution happens slowly and smoothly

## Fitness Functions and the Selection Environment 

- Fitness function and selection environments are the two faces of fitness and they are intricately connected
    - Fitness of an individual is relative to a particular environment and to the measure (fitness function) used to evaluate them 
- Success of a problem not only depends on the fitness function, but also on quality of selection environment 

### The Selection Environment 

- Selection environment is the input to the evolutionary system
- Models will depend greatly on the quality of the environment we choose for them to blossom 
- First requirement is a set of fitness cases representative of the problem at hand
- Second consists of a all-balanced set, to avoid the creation of models that can only solve a partial marginal aspect of the overall problem
- Even with a good data set, it is possible to get stuck in local optima, and individuals might need a little help
- To do this, we can change our fitness function
    - This changes the fitness landscape, and a peak can become a valley, leading to better solutions
- It is handy to have more than one fitness function at our disposal to try a few of them on a problem 

### Fitness Functions for Symbolic Regression

- An important application of evolutionary computation is symbolic regression, where the goal is to find a model that is good at numeric prediction (will perform well for all fitness cases)
- There are several measures to evaluate how good these models are
    - Some are based on the absolute error between predicted and target values
    - Others are based on relative error
    - Others are based on statistical indexes that measure correlation between values
- Depending on the problem, any fitness function could perform better or worse than others, but some functions like mean squared error or R-square are universal, and can be used to evolve very good models in all kinds of problems
- Remember, absolute error is `abs(p - t)` and relative error is `abs((p - t) / t)`, where `p` is predicted value, and `t` is target value

#### Number of Hits

- Favors Models that perform well for all fitness cases within a certain error (absolute or relative)
- Formally, fitness `f(i, j)` of an individual program `i` for fitness case `j` is evaluated by:
    - `If err(i, j) <= p, then f(i, j) = 1, else f(i, j) = 0`
    - where `p` is precision error, and `err(i, j)` is error on individual program `i` for test case `j` 

#### Precision and Selection Range

- Idea of a selection range and a precision. 
    - Selection range is used as a limit for selection to operate
    - Precision is the limit for improvement
- Formally, fitness `f(i)` of an individual program `i` is expressed by:
    - `f(i) = sum_j_from_1_to_n(R - err(i, j))`
    - Where `R` is the selection range and `err(i, j)` is error for test case `j` with individual `i`
    - The error term is called the precision `p`

#### Mean Squared Error

- Based on standard mean squared error
- Formally, mean squared error `E(i)` of an individual program `i` is:
    - `E(i) = 1 / n * sum_j_from_1_to_n(err(i, j)^2)`
- As it stands, `E(i)` cannot be used directly to measure fitness, as fitness must increase with efficiency (in this case it is reduced).
- Thus, to evaluate fitness `f(i)` of an individual `i`, the following equation is used
    - `f(i) = 1000 * 1 / (1 + E(i))`
    - It ranges from 0 to 1000, with 1000 being the ideal 

#### R-Square

- Based on standard R-square, that returns square of Pearson product moment correlation coefficient
    - This coefficient ranges from -1 to 1, and reflects the extent of a linear relationship between predicted and target values. 1 means perfect correlation, -1 is a perfect negative correlation. 0 means no correlation
- Formally, the Pearson product moment correlation coefficient `R(i)` of an individual program `i` is evaluated by:
- <p align="center"><img src="./img/3.6.png" width="300"/></p>
- Where `P(i, j)` is predicted value by individual `i` for fitness case `j`, and `T(j)` is target value for fitness case `j`
- Then, fitness `f(i)` of individual `I` would be
    - `f(i) = 1000 * R(i)^2`

