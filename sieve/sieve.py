""" The Sieve of Eratosthenes is a simple, ancient algorithm 
for finding all prime numbers up to any given limit. 
It does so by iteratively marking as composite (i.e. not prime) 
the multiples of each prime, starting with the multiples of 2. 

It does not use any division or remainder operation.

Create your range, starting at two and continuing up to 
and including the given limit. (i.e. [2, limit])

The algorithm consists of repeating the following over and over:

. take the next available unmarked number in your list (it is prime)
. mark all the multiples of that number (they are not prime)

Repeat until you have processed each number in your range.
When the algorithm terminates, all the numbers in the list 
that have not been marked are prime.
 """

def sieve(limit):
    my_list = [num for num in range(2, (limit+1))]
    #move to next n(num), 2(2)=4, my_list[num(n)], mark with -1
    for num in my_list:
        for i in range((num-1)*2, len(my_list), num):
            my_list[i] = -1
    
    my_list = [num for num in my_list if num != -1]

    return my_list
