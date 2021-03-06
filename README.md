# PrimeOptimus
****Multiprocessing Prime Number Finder****
```
Some of this code requires an extra non-default Python module to run named: mpmath.
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
Python version 3.8.7 (64-bit)

This computer-system has (16) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter number for Prime test: (2**61)-1
Calculating...
Progress: [■■■■■■■■■■] 10/10 
Finished processing in 21.6 seconds.
Number: 2305843009213693951
Prime: Yes
Length: 19
Do you want to calculate if another number is Prime? (y/n): 
```
2 quintillion 305 quadrillion 843 trillion 009 billion 213 million 693 thousand 951 is a Prime number ***for certain*** because the program fully calculated all possible divisors with separate parallel processes in 21.6 seconds. Now lets try the same number but +1:
```
Python version 3.8.7 (64-bit)

This computer-system has (16) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter number for Prime test: (2**61)+1
Calculating...
Progress: [■■■■■■■■■■] 10/10
Finished processing in 0.2 seconds.
Number: 2305843009213693953
Prime: No
Length: 19
Do you want to calculate if another number is Prime? (y/n): 
```
Notice the time 0.2 seconds. The input number was the same but + 1. The algorithm terminates when any of the parallel processes returns a divisible number. This means that if the number is Prime, the processes will be running much longer as it continues to search for a divisor. With this method it is possible to make better predictions of large Primes without too much computing. Any number entered that is not Prime will return within a few seconds because of the way the algorithm works. The more threads your system has, the more certainty given to a Prime prediction without a full computation. Fish for a Prime by inspecting a number from multiple vantage points simultaneously.

Here is output from PrimeFinder.py:
```
Python version 3.8.7  (64-bit)
This computer-system has (16) logical processors for this prime task.
This is a multiprocessing prime number program written by zachap@gmail.com.
A single number will be evenly split (16) times across its domain to be sampled
by simultaneous calculations on separate cores checking the number for factors.

Initializing...
Do you want to test for probable primes?: n

Examples of prime number functions in python: 
Kynea primes: (2**n+1)**2-2
Mersenne primes: (2**n)-1
Zach primes: 2*(n**2)-1

Enter prime number FUNCTION:(2**n+1)**2-2
Enter the number for 'n' START:0
Enter the number of ITERATIONS:33
Progress: ########## 100%
Primes:
ƒ(0) = 2
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
Primes found: 15
Prime at end of list has 20 digits.
Overall process took 1 minute and 52.6 seconds.
Initializing...
Do you want to test for probable primes?: 
```
The last number ƒ(32) took about the same amount of time to calculate as all the previous calculations combined. 18446744082299486207 (18.44 quintillion)
Due to my core count potential. For faster calculations beyond (with a slower computer) the program also has a "probable primes" setting:
```
Python version 3.8.7  (64-bit)
This computer-system has (16) logical processors for this prime task.
This is a multiprocessing prime number program written by zachap@gmail.com.
A single number will be evenly split (16) times across its domain to be sampled
by simultaneous calculations on separate cores checking the number for factors.

Initializing...
Do you want to test for probable primes?: y

How many loop-steps do you want a multiprocess to continue to
multi-core-sample a number that has not found an immediate factor?
Larger numbers increase odds of finding a 'more potential' prime.
Can be entered as (2**23) where (**) is raising to the exponent.
Maximum multiprocess STEPS: 2**20

Examples of prime number functions in python: 
Kynea primes: (2**n+1)**2-2
Mersenne primes: (2**n)-1
Zach primes: 2*(n**2)-1

Enter prime number FUNCTION:(2**n+1)**2-2
Enter the number for 'n' START:0
Enter the number of ITERATIONS:50
Progress: ########## 100%
Potential primes:
ƒ(0) = 2
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
ƒ(36) = 4722366483007084167167
ƒ(48) = 79228162514264900543497371647
'Potential' primes found: 17
'Potential' prime at end of list has 29 digits.
Overall process took 23.9 seconds.
Initializing...
Do you want to test for probable primes?: 
```
The program trimmed down a list of *probable primes* with a precision of 2^20 and found 47 possible primes from 0-50 in ƒ(n) = (2^n+1)^2-2. In a future commit, the distribution of prime numbers posed by the prime number theorem will be implemented alongside prime counting functions to estimate which probable primes should be deducted from the list at the end. I am also pondering a way to implement the Riemann Zeta function as a helper, but it slows things down quite a bit with large numbers.

This program works better on a linux system because it opens and closes processes rapidly for each iteration. Windows has trouble with this. 

I have made a rewrite specially for windows named PrimeOptimus.py which opens a number of processes equal to the logical core count of your computer and keeps them open to feed data in and out instead. This version is much faster for making large lists of smaller primes. The only issue with this version: I can't effectively stop a Task object process after it has started without stopping and starting processes again. The reason you would want to is because if a Task object returns a zero, all the other Task objects are wasting their time on a segregation of the same number. I am working on a method.
Here is an output:
```
Enter prime number FUNCTION:n
Enter the number for 'n' START:1
Enter the number of ITERATIONS:100000
Progress: ########## 100%
Primes:
ƒ(2) = 2
ƒ(3) = 3
ƒ(5) = 5
ƒ(7) = 7
ƒ(11) = 11
ƒ(13) = 13
ƒ(17) = 17

....etc...etc....

ƒ(99901) = 99901
ƒ(99907) = 99907
ƒ(99923) = 99923
ƒ(99929) = 99929
ƒ(99961) = 99961
ƒ(99971) = 99971
ƒ(99989) = 99989
ƒ(99991) = 99991
Primes found: 9592
Prime at end of list has 5 digits.
Overall process took 47.0 seconds.
```
It found all 9592 primes from 1 to 100000 in 47.0 seconds and is 100% accurate since it divided everything in parrallel across my 8 hyperthreaded cores.
You can clarify that there is 9592 primes between 10^0 and 10^5 in the table on https://en.wikipedia.org/wiki/Prime-counting_function.

To speed it up even further we enter the function (n+n)-1 to skip all even digits including 2:
```
Enter prime number FUNCTION:(n+n)-1
Enter the number for 'n' START:1
Enter the number of ITERATIONS:50000
Progress: ########## 100%
Primes:
ƒ(2) = 3
ƒ(3) = 5
ƒ(4) = 7
ƒ(6) = 11
ƒ(7) = 13
ƒ(9) = 17

....etc...etc....

ƒ(49951) = 99901
ƒ(49954) = 99907
ƒ(49962) = 99923
ƒ(49965) = 99929
ƒ(49981) = 99961
ƒ(49986) = 99971
ƒ(49995) = 99989
ƒ(49996) = 99991
Primes found: 9591
Prime at end of list has 5 digits.
Overall process took 23.8 seconds.

```
Now it only took 23.8 seconds to find all primes from 1 to 100000 with a count of 9591 which is one less than 9592 since the function (n+n)-1 took away the only even numbered prime (2) at the beginning.

If you think thats impressive, this is an output from the MersennePrime.py finder:
```
For Mersenne (2^n)-1 enter ƒ(n):44497
Progress: ■■■■■■■■■■ 100% 
(2^44497)-1
Prime: YES.
Length: 13395 digits.
Overall process took: 1 minute and 47.5 seconds.
```
Yes it only took 1 minute and 47.5 seconds to confirm a Mersenne prime number of 13395 digits long. To put it in perspective, imagine 1 followed by 13395 zeros.
This program only confirms Mersenne Primes which are easier to pinpoint due to their symmetrical location being 1 less than a power of 2 which alternate as squares.
The genius is in the algorithm of which I did not find myself. I only rewrote it.
I have attempted to make it parallel processing, but all attempts have only made it slower since
each iteration is based on a previous unknown modulus. The answer may be multiprocessing the modulus operator itself. Though I don't think it would be very efficient because you would have to do setup work for each process before the actual modulus computation even begins. The answer may just be a super high GHZ single core CPU for this particular algorithm.
This website shows all Mersenne Primes that have been proven:
https://www.mersenne.org/primes/
(2^44497)-1 is listed.
I would rather use my own program to find prime numbers because I know how it works and I when their program runs on your computer when you reach 99% complete with this algorithm, they could easily upload your current modulus and take the find from you.

In a future commit, a version of the program will be able to save files as tables of prime number sequences generated from lists of functions ordered by their "sequential prime spread" to build a database that can grow big-data as pure combinations of prime number equations. It will attempt to utilize Goldbach's conjecture.
