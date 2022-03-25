# Parameter Optimization

- GAs have been used for parameter optimization, encoding values of parameters on the chromosomes 
- GEP can also be used to do parameter optimization very efficiently, and this chapter introduces two algorithms to do this
    - HZero algorithm
    - GEP-PO Algorithm

- HZero algorithm is very similar to GA, as it uses candidate parameters directly. This is more flexible that GA and easier to implement, it is quick and straightforward, but that point is not always the best and this algorithm has a hard time getting out of there 
- GEP-PO algorithm is not afflicted by this problem, as it designs the parameter values with mathematical operators and varieties of random numerical constants. This gives it much more precise tools for fine tuning parameter values, and to search peaks and valleys of solution space, increasing odds of finding global optimum 
-  Both algorithms explore RNCs and multigenic nature of GEP to find parameters that optimize a multidimensional function. 
- Each parameter value is encoded in a different gene. 
    - For `N` parameters, we use `N` genes 

## The HZero Algorithm 

- Implementation of GEP-RNC algorithm as its utmost simplicity, with head size equal to zero, a tail of 1, and Dc length of 1 too. 
- Dc's in HZero algorithm have just one element, and it is easier to implement than simple GAs, but have advantages of flexible evolution 

### Architecture 

- A normal gene with `h` = 0 with a Dc domain has the following structure
    - `?3`
    - where `?` represent the ephemeral random constants, and `3` is a numerical representing an index pointing to a specific random numerical constant 
    - For example, gene above chooses RNC in position 3 in the array/set of RNCs
- For multidimensional optimization task, we use multigenic chromosomes, where each gene has its own array of RNCs
    - An example could be `?2?4?1`
- The parameters obtained from the chromosome are used to find max or min of a function 
- Each chromosome in a parameter optimization task encodes a particular set of parameter values, evaluating itself with the function result, which can be used as fitness 
    - To avoid having 0 or negative fitness, the worse-of-generation fitness `f_min` is added in absolute value to all fitness of individuals (Just if `f_min` is negative, we add `abs(f_min) + 1` 
    - This guarantees we have all positive fitness, to reproduce and select individuals as needed 

### Optimization of Simple Function 

- This is more flexible than GA, as we can change values of RNCs to try to find optimum
- Usually 10 constants per gene is enough
- In parameter optimization, we try to find the parameters than maximize (or minimize) a complex multidimensional function 
    - If need to minimize, we can multiply function by -1 and maximize
    - We use max as we usually favor higher fitness
- To test it, we can use a simple function defined as:
    - `f(x) = x + sin(10 * pi * x) + 1.0`
- The goal is to find value of `x_0` that maximizes function  
- This problem uses 5 RNCs
- Due to structure, it can only benefit from mutation 
    - Multidimensional optimization uses two-point recombination, gene recombination, gene transposition for tuning too
- Using this, global maximum was found in 8 generations

## GEP-PO Algorithm 

- Considerably more complex that either HZero algorithm or GA, as it explores GEP-RNC in all its complexity
- This makes use of complex genes for fine tuning of parameters that optimize the function 
- Rarely stuck in local optima for Long stretches of time 

### Architecture

- Similar to HZero, it uses `N` different genes to encode all parameters to optimize
- Here genes are more complex, as each one has a head bigger than 0,and it uses functions and RNCs

### Optimization of Simple Function

- Using the same function as before, we try to optimize 
- Perfect solution found in generation 6
- This kind of learning and tuning is not possible with HZero, as each parameter is just one node 
- Even with more generations, we can get better and better approximations 
- Performed better than HZero

## Maximum Seeking with GEP

- Now, we try to find maximum of two different functions
- First one is 
    - `f(x, y) = - x * sin(4x) - 1.1 * y sin(2y)`
- For first one, both HZero and GEP-PO found global optimum 
- HZero outperformed GEP-PO in this simple task, as populations evolved quicker
- Here it would be advisable to use simpler HZero, when we have one or two dimensions 
- However GEP-PO can find much more precise parameter values, so when precision is needed, we should use GEP-PO, as HZero can also get trapped on local optimums 
- GEP-PO can approximate global maximum even better than HZero 

- Now, using a much more difficult task with 5 parameters, we can try both algorithms again 
- As expected, GEP-PO performs slightly better, with this advantage residing on the fine-tuning capabilities  
