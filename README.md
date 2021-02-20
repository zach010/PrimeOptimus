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
Notice the time 0.2 seconds. The input number was the same but + 1. The algorithm is smart enough to terminate when any of the parallel processes returns a divisible number. This means that if the number is Prime, the processes will be running much longer as it continues to search for a divisor. With this method it is possible to make good predictions of large Primes without too much computing. Any number entered that is not Prime will return within a few seconds because of the way the algorithm works. The more threads your system has, the more certainty given to a Prime prediction without a full computation. Fish for a Prime by inspecting a number from multiple vantage points simultaneously.

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
Overall process took 1 minute and 45.5 seconds.
Initializing...
Do you want to test for probable primes?: 
```
The last number ƒ(32) took a long time to modulus all numbers from 1 to 18446744082299486207 into 18446744082299486207 (18 quintillion)

The program also has a "probable primes" setting:
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
Enter the number for 'n' START:1
Enter the number of ITERATIONS:200
Progress: ########## 100%
Potential primes:
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
ƒ(51) = 5070602400912922109586440191999
ƒ(60) = 1329227995784915875209650069494038527
ƒ(65) = 1361129467683753853927285406021911052287
ƒ(71) = 5575186299632655785388651934644960021708799
ƒ(74) = 356811923176489970264609271294236741257396223
ƒ(75) = 1427247692705959881058361527313221050706165759
ƒ(80) = 1461501637330902918203687250567922248914281955327
ƒ(87) = 23945242826029513411849172608708590815387867508899839
ƒ(93) = 98079714615416886934934209757426828380165388218136526847
ƒ(95) = 1569275433846670190958947355881144766539853198709552578559
ƒ(96) = 6277101735386680763835789423366122741130884119651122413567
ƒ(98) = 100433627766186892221372630771956487957751801812172903809023
ƒ(99) = 401734511064747568885490523086558301230778977847194912030719
ƒ(105) = 1645504557321206042154969182557431634621150472315275652353753087
ƒ(110) = 1684996666696914987166688442938729513250750793822600045317140250623
ƒ(111) = 6739986666787659948666753771754912860706144640462771650772231782399
ƒ(113) = 107839786668602559178668060348078543463736011829472804046399757877247
ƒ(116) = 6901746346790563787434755862277025618604608445284870668138406758842367
ƒ(117) = 27606985387162255149739023449108102142111434834910514446601861965283327
ƒ(137) = 30354201441027016733116592294117482916287955309333407060546155397768389586979913727
ƒ(138) = 121416805764108066932466369176469931665151124339046174160211448599877538086622593023
ƒ(143) = 124330809102446660538845562036705210025114060000082127890739135759008146901494849863679
ƒ(150) = 2037035976334486086268445688409378161051468396520431636048060211470953238662326978948890623
ƒ(170) = 2239744742177804210557442280568444278121645497234652528055342354652968352326698348328501748621455130623
ƒ(173) = 143343663499379469475676305956380433799785311823017594178842128491196091604702599727957153612181639528447
ƒ(179) = 587135645693458306972370149197334256843920637227079969209318283748941114636999138016233933214931297941585919
ƒ(180) = 2348542582773833227889480596789337027375682548908319873772282053263986741831302497764317365622246947399139327
ƒ(183) = 150306725297525326584926758194517569752043683130132471749786550831915599341068492816081682834525022948981473279
ƒ(188) = 153914086704665934422965000391185991426092731525255651047457658827258185765390452628737935860156996152458894901247
ƒ(192) = 39402006196394479212279040100143613805079739270465446667960847607716495133024882190260681587717120351695556059332607
ƒ(197) = 40347654345107946713373737062547060536401653012956617387979454180458683841582029156611293935652784166934432760283004927
'Potential' primes found: 47
'Potential' prime at end of list has 119 digits.
Overall process took 1 minute and 48.6 seconds.
```
The program trimmed down a list of *probable primes* with a precision of 2^20 and found 47 possible primes from 1-200 in ƒ(n) = (2^n+1)^2-2
In a future commit, the distribution of prime numbers posed by the prime number theorem will be implemented alongside prime counting functions 
to estimate which probable primes should be deducted from the list at the end. I am also pondering a way to implement the Riemann Zeta function 
as a helper, but it slows things down quite a bit with large numbers. This program works better on a linux system because it opens and closes 
processes rapidly for each iteration. Windows has trouble with this. I have thought of a rewrite specially for windows using class object processes 
that I can keep open and just pickle, but I can't figure out how to efficiently stop a set of processes from continuing resource calculation without 
terminating them and having to reopen them.

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
This website shows all Mersenne Primes that have been proven:
https://www.mersenne.org/primes/
(2^44497)-1 is listed.
I would rather use my own program to find prime numbers because I know how it works and I when their program runs on your computer when you reach 99% complete with this algorithm, they could easily upload your current modulus and take the find from you.

