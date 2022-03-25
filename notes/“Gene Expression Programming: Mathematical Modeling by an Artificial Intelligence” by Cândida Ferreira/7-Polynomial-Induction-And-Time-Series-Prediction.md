# Polynomial Induction and Time Series Prediction 

- This chapter explores the idea of domains of random numerical constants in order to evolve high-order multivariate polynomials
- Then, discuss the importance of Kolmogorov-Gabor Polynomials in evolutionary modeling by comparing performance of this new algorithm `GEP-KGP` (GEP for inducing Kolmogorov-Gabor polynomials) with much simpler and intelligible GEP systems 

## Evolution of Kolmogorov-Gabor Polynomials 

- Kolmogorov-Gabor Polynomials have been widely used to evolve general nonlinear models 
- Evolving such polynomials with GEP is very simple and only requires the implementation of special functions of two arguments. 
- For instance, a special function `F` that receives two arguments could correspond to the following mathematical expression 
    - `y = a_0 + a_1 * x_1 + a_2 * x_2 + a_3 * x_1 * x_2 + a_4 * x_1 ^ 2 + a_5 * x_2 ^ 2`
- The six coefficients can be easily evolved using a special domain `Dc` for handling random numerical constants
- As for the GEP-RNC algorithm, the Dc comes after the tail, but in this case, has a length equal to `6h` in order to cover for all the cases, including when all nodes in head are function nodes requiring the maximum value of six coefficients 
- For example, consider the following chromosome, with `h` = 2
    - `FFabc252175089728`
    - the Dc in the chromosome is `252175089728`, where numerals represent polynomial coefficients chosen from the set of random numerical constants 
    - `C = {-0.606, -0.398, -0.653, -0.818, -0.047, 0.036, 0.889, 0.148, -0.377, -0.841}`
    - Then, values can be replaced with indexes 
- These polynomials might become really complex

## Simulating STROGANOFF in GEP

- The two parameter function `F` given above is used in the `STROGANOFF` system
- By choosing this function, we simulate the original STROGANOFF system in GEP (GEP-OS)
- Other functions (polynomials) can be added to create the enhanced STROGANOFF (GEP-ES)
- We can create genes to simulate this, like the following:
    - `F9.d6.F7.d8.d2.d0.d5`
    - where F# is a function with a number to know which one, and d# is a Dc position for the chosen random number

- Due to huge dimensions of random constants, it is important to control degree of genetic variation in them 
- Special mutation operators were implemented that allow autonomous control of mutation rate

    
## Evaluating Performance of STROGANOFF 

- In this section, we evaluate performance of various STROGANOFF systems, by comparing them with four simpler GEP systems (with/without RNCs, basic GEA/cellular system) using the sunspots problem 

### Original and Enhanced STROGANOFF

- Original consists of just one kind of function, but this function will be weighted 16 times to compare with enhanced implementation, that uses 16 functions
- 40 RNCs will be used per gene (120 total in multigenic), and 120 RNCs
- As expected, enhanced implementation is considerably better that original STROGANOFF
- Multigenic system works considerably better than unigenic one
- Without RNCs, systems get trapped on local optimum and it can't escape 
- Polynomials are extremely complex, making it almost impossible to extract knowledge from them 

### Simpler GEP Systems

- Using just `{+, -, *, /}` (weighted 4 times to have 16) instead of polynomials, we get all of our systems performing quite well at this difficult task and considerably better than all STROGANOFF systems studied in 
- Presence on RNCs result in slight increase in performance in both acellular and cellular systems 
- Conclusions 
    - A STROGANOFF like system exploring second order bivariate basis polynomials is extremely inefficient in evolutionary terms
    - It has worse performance and much more structural complexity 
    - Any conventional GEP system with simple arithmetic functions is much more efficient and simpler that STROGANOFF systems 
- Then, we can use simplest of GEP systems to design a model to predict sunspots with

## Predicting Sunspots with GEP

- Time series analysis is a special case of symbolic regression 
    - Thus, can be solved with GEP
- Time series have data that represent series of observations taken at time intervals, and the idea is to use past observations to predict future ones 
- In practical terms, we are trying to find a prediction model that is a function of a certain number of past observations
    - We call number of past observations `d`
    - We will use `d`= 10
- We also have a delay timer `t` that determines how data is processes 
    - a delay time of one means data is processed continuously, whereas higher value of `t` indicates some observations are skipped
- e can use `t-10` through `t-1` as independent variables and `t` as dependent 

- Using GEP, we can simulate the process, and obtain good predictions reaching an R-squared of 0.94 on train and 0.87 on test
- This method of approaching a complex function by introducing one term at a time seems creative and useful to design predictive models 


