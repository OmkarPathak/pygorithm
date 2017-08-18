"""
Author: OMKAR PATHAK
Created at: 16th August 2017

Sieve of Eratosthenes is one of the efficient algorithms to find all the prime numbers up to n, where n can be
up to 10 million. This algorithm is very efficient and fast and hence is preferred by many competitive programmers.

Algorithm:
1. Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
2. Initially, let p equal 2, the first prime number.
3. Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list.
   These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise,
   let p now equal this number (which is the next prime), and repeat from step 3.
When the algorithm terminates, all the numbers in the list that are not marked (i.e are True) are prime.
"""
import inspect


def sieve_of_eratosthenes(n):
    """
    function to find and print prime numbers up
    to the specified number

    :param n: upper limit for finding all primes less than this value
    """
    primes = [True] * (n + 1)
    # because p is the smallest prime
    p = 2

    while p * p <= n:
        # if p is not marked as False, this it is a prime
        if primes[p]:
            # mark all the multiples of number as False
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1

    # getting all primes
    primes = [element for element in range(2, n) if primes[element]]

    return primes


def get_code():
    """
    returns the code for the sieve_of_eratosthenes function
    """
    return inspect.getsource(sieve_of_eratosthenes)
