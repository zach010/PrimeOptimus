# PrimeOptimus
****Multiprocessing Prime Number Finder****
```
This code requires an extra non-default Python module to run named: mpmath.
```
Prime.py takes an input from a user and splits the input into smaller chunks across a 
group of parallel processes that is equal to the total logical processors in your system.
```
Support for exponental equation entry examples: 
Mersenne Prime Format: 2**x-1
Kynea Prime Format: (2**x + 1)**2-2
Or any format with Pythonic syntax.
```
Example output as a test for a Mersenne Prime that is a power of 2 minus 1:
```
Python version 3.7.1 (64-bit)

This computer-system has (8) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter number for Prime test: 2**61-1
Calculating...
Progress: [■■■■■■■■■■] 10/10 
Finished processing in 1 minute and 10.2 seconds.
Number: 2305843009213693951
Prime: Yes
Length: 19
Do you want to calculate if another number is Prime? (y/n): 
```
2 quintillion 305 quadrillion 843 trillion 009 billion 213 million 693 thousand 951 is a Prime number ***for certain*** because the program fully calculated all possible divisors with separate parallel processes in 1 minute 10 seconds. Now lets try the same number but +1:
```
Python version 3.7.1 (64-bit)

This computer-system has (8) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter number for Prime test: 2**61+1
Calculating...
Progress: [■■■■■■■■■■] 10/10
Finished processing in 0.2 seconds.
Number: 2305843009213693953
Prime: No
Length: 19
Do you want to calculate if another number is Prime? (y/n): 
```
Notice the time 0.2 seconds. The input number was the same but + 1. The algorithm is smart enough to terminate when any of the parallel processes returns a divisible number. This means that if the number is Prime, the processes will be running much longer as it continues to search for a divisor. With this method it is possible to make good predictions of large Primes without too much computing. Any number entered that is not Prime will return within a few seconds because of the way the algorithm works. The more threads your system has, the more certainty given to a Prime prediction without a full computation. Fish for a Prime by inspecting a number from multiple vantage points simultaneously.

Here is output from PrimeFinder.py:
```
Examples of prime number functions in python: 
Kynea primes: (2**n+1)**2-2
Mersenne primes: (2**n)-1

Enter prime number FUNCTION:(2**n+1)**2-2
Enter the number for 'n' START:1
Enter the number of ITERATIONS:32
Progress: ■■■■■■■■■■ 100%
Primes:
ƒ(1) = 7
ƒ(2) = 23
ƒ(3) = 79
ƒ(5) = 1087
ƒ(8) = 66047
ƒ(9) = 263167
ƒ(12) = 16785407
ƒ(15) = 1073807359
ƒ(17) = 17180131327
ƒ(18) = 68720001023
ƒ(21) = 4398050705407
ƒ(23) = 70368760954879
ƒ(27) = 18014398777917439
ƒ(32) = 18446744082299486207
Primes found: 14
Prime at end of list has 20 digits.
Overall process took 1 minute and 41.3 seconds.
Initializing...
Do you want to test for probable primes?: 
```
This code could be used for encryption or compression algroithms by saving data as straight math formulas.

This is an output from the MersennePrime.py finder:
```
For Mersenne (2^n)-1 enter ƒ(n):44497
Progress: ■■■■■■■■■■ 100% 
(2^44497)-1
Prime: YES.
Length: 13395 digits.
Overall process took: 1 minute and 47.5 seconds.
```
Yes it only took 1 minute and 47.5 seconds to confirm a Mersenne prime number of 13395 digits long.
This program only confirms Mersenne Primes though.
The genius is in the algorithm of which I did not find myself. I only rewrote it.
I have attempted to make it parralel processing, but all attempts have only made it slower since
each iteration is based on a previous unknown modulus that cannot be set up very efficiently in python.
