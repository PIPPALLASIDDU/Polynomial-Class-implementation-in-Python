# Polynomial-Class-implementation-in-Python
Polynomial Class function implementation with Python OOPS - overloading plus , minus , assignment and multiplication operators 

Problem Statement :
Implement a polynomial class with the following properties and functions. 
Properties : 
1. An integer (lees say A) which holds the coefficient and degrees. Use array indices as degree and A[i] as the coefficient of ith degree. 
2. An integer holding the total size of array A. 
Functions : 
1. Default Constructor 
2. Copy Constructor 
3. SetCoefficient -This function sets coefficient for a particular degree value. If the given degree is greater than the current polynomial capacity, increase the capacity accordingly and set the required coefficient. If the degree is within limits, the previous coefficient value is replaced by the given coefficient value. 
4. Overload "+" Operator (P3 = P1 + P2) : Adds two polynomials and returns a new polynomial that has the result. 
5. Overload "-" Operator (P3 = P1- P2) : Subtracts two polynomials and returns a new polynomial which has the result 
6. Overload * Operator (P3 = Pi * P2) : Multiplies two polynoc and returns a new polynomial which has the result 
7. Overload "=" Operator (Copy Assignment Operator) -Assigns all values of one polynomial to another. 
8. Print() -Prints all the terms (only terms with non zero coefficients are to be printed) in increasing order of degree. Print Pattern For A Single Term : <Coefficient>"X"<Degree> Ana multiple terms should be printed separated by space. And after printing one polynomial, print a new line. For more clarity, refer to sample test cases. 
Sample Input 2 :
3
1 3 5
1 2 -4
4
0 1 2 3
4 2 -3 1
2(subtraction)
Sample Output 2 :
-4x0 -1x1 3x2 1x3 -4x5
