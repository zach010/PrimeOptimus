# PrimeOptimus
****Multiprocessing Prime Number Finder****
```
This Code requires an extra non-default Python module to run named: mpmath.
```
The code takes an input from a user and splits the input into smaller (quicker to calculate) numbers
across a group of parallel processes that is equal to the count of the logical processors on your system.
```
Support for exponental equation entries of the form: x ^ y ± z
```
Example output as a test for a Mersenne Prime that is a power of 2 minus 1:
```
Python version 3.7.1 (64-bit)

This computer-system has (8) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter the number for a Prime check : 2^61-1
Calculating...  
Progress: ►■■■■■■■■■■◄ 10/10 
Finished processing in 2 minutes and 29.7 seconds.
Number: 2305843009213693951.0
Prime: Yes.
Length: 19
Do you want to calculate if another number is Prime? (y/n): 
```
2 quintillion 305 quadrillion 843 trillion 009 billion 213 million 693 thousand 951 is a Prime number ***for certain*** because the program fully calculated all possible divisors with separate parallel processes in 2 and a half minutes. Now lets try the same number but +1:
```
Python version 3.7.1 (64-bit)

This computer-system has (8) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter the number for a Prime check : 2^61+1
Calculating...  
Finished processing in 0.4 seconds.
Number: 2305843009213693953.0
Prime: No.
Length: 19
Do you want to calculate if another number is Prime? (y/n): 
```
Notice the time difference with the same number + 1.
The algorithm is smart enough to terminate when any of the parallel processes returns a divisible number.
This means that if the number is Prime, the processes will be running much longer as it continues to search for a divisor.
With this method it is possible to make good predictions of large Mersenne Primes without too much computing. 
Any number entered that is not Prime will return within a few seconds because of the way the algorithm works.
The more threads your system has, a number will get a broader spectrum of parallel sampling spread across its 
domain giving even more strength to a Prime prediction without need for full a computation. 
Fish for a Prime by inspecting the number from multiple vantage points simultaneously.
(I am working on a Cuda Version) Do you like fried Cuda?
```
The code also accepts scientific notation input:
```
Sample Output:
```
Python version 3.7.1 (64-bit)

This computer-system has (8) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter the number for a Prime check : 1.0e+100000
Calculating...  
Finished processing in 0.7 seconds.
Number: 1.0e+100000
Prime: No.
Length: 100001
Do you want to calculate if another number is Prime? (y/n): 
```
With my 8-thread computer, numbers with one hundred thousand trailing zeros appear to be the limit in size before the program becomes extremely slow.

