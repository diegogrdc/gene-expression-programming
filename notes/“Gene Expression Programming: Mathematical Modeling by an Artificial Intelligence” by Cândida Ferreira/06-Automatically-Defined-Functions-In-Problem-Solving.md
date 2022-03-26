# Automatically Defined Functions in Problem Solving 

- ADFs were introduced as a wey of reusing code in genetic programming 
- In GEP, we can use ADFs in a special gene called `homeotic gene`
- Product of this gene consists of the main programs or cell 
- Homeotic genes determine which genes are expressed in which cell, and how different sub ET-s interact between them
    - Now, sub-ETs work as ADFs
- Homeotic genes determine which ADFs are called upon in main program, and how these ADFs are organized in each main program 

## Homeotic Genes

- Remember, for homeotic genes, the terminals are numbered for every ADF encoded in conventional genes 
    - For example, if we had two regular genes, and the extra homeotic gene, the alphabet would be `T_h = {0, 1}`, with each number representing the whole sub-ET on a gene
- A chromosome can have multiple cells (or homeotic genes), and we keep the best value, similar to a multigenic chromosome
    - For example, we can have two homeotic genes, each encoding a program, and after evaluation we keep the best one  
    - It is also possible to just have one homeotic gene as main program
- Homeotic genes help generate modular solutions, similar to UDFs, but with more flexibility, and most times with better results

## Experiments

- Using a few examples, the following algorithms performance was compared
    - GEA with just one gene (UGS)
    - GEA with multigenic system composed of two genes linked by multiplication (MGS)
    - Cellular system with two ADFs (MCS)

### Kepler's Third Law 

- On Keplers Third Law, success rates obtained on experiment were
    - UGS -> 76%
    - MGS -> 96%
    - MCS -> 99%
- For simple problems, cellular system is extremely flexible and allows efficient evolution 

### Incorporating RNCs in ADFs

- On analog circuits, where numerical constants are necessary we need a way of incorporating RNCs in ADFs
- We use the same structure seen on chapter 5, by creating the Dc domain for each gene.
    - For simplicity, they are only added on genes encoding ADFs, but they can be extended to be a part of homeotic genes too
    - However, not a lot is gained, and the increase in computational effort could be significant	
- Genes encoding ADFs are expressed exactly as normal genes with Dc domain, and homeotic genes call them as usual 
- Now, using analog circuit problem we can compare performance with a unicellular system (UCS) that uses RNC or not
- As expected, UCS with RNCs performs considerably better than simpler UCS at this task, with a success rate of 89.6% with RNCs, and 67% without
    - It performs better, but it is also slower than its counterpart, as these systems obviously require more time or larger populations to fine-tune their complex structures
    - Also note that even simple UCS can get to good solutions (93%) even though it is harder to find
    - Best solution found by UCS-RNCs was 95.9%
- Also, Cellular systems allow dynamic linking systems, which are another advantage 
- Usually, models with RNCs are much more compact and are also usually less varied in terms of function nodes in their construction 

### Diagnosis of Breast Cancer

- Remember this is a classification problem
- To look for solutions, multi cellular systems were used, with and without RNCs
- Average best of run fitness was pretty similar, (around 339/1000), corroborating that numbers are not important in this specific problem 
- We found out that adaptation of cellular systems occurs more slowly than simpler systems without ADFs
- However, with more time or larger populations, good solutions can be found with cellular systems
- Best solution without RNCs got 98.8% classification accuracy on testing set, and 88.2% with RNCs

### Iris Problem 

- Problem with multiple outputs
- Before, all cells were engaged in finding same kind of solution, and we kept the best cell performance
- Here, we can use `n` different cells to classify `n` different classes
- Fitness of individual will depend on accuracy of the different submodes expressed in different cells 
    - This is similar to what we have seen before, but here we can have as many ADFs as we want, and reuse them on each classification gene  
- Using this setup, a multicellular system with multiple outputs (MCS-MO) is extremely efficient, surpassing multigenic systems with multiple outputs considerably (147.2 vs 146.48)
- Best model of experiment classified 149/150 correctly (99.33% accuracy)
- Models are more compact thanks to code reuse 

  
