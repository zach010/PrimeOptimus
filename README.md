# PrimeOptimus
****Multiprocessing Prime Number Finder****
```
This Code requires an extra non-default Python module to run named mpmath.
```
The code takes an input from a user and splits the input into smaller (quicker to calculate) numbers
across a group of processes that is equal to the count of logical processors on your system.
```
Sample Output:
Python version 3.7.1 (64-bit)

This computer-system has (8) logical processors initialized for this Prime task.
Do you want to calculate if a number is Prime? (y/n): y
Enter the number for a Prime check : 18014398777917439
Calculating...  
Progress: ►■■■■■■■■■■◄ 10/10 
Finished processing (18014398777917439.0) in 15.3 seconds.
18014398777917439.0 is Prime.
```
When a process finishes and returns 1, it will leave a core idle.
My goal is to make the other processes smart enough to realize a
extra core is available and distribute some of their processing load
to the freed up cores. I might be able to do it with Daemon child processes
that can branch off.

