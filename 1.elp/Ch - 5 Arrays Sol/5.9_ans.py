# Enumerate all primes to n

# Write a program that takes an integer argument and returns all the primes between 1 and that 
# integer. For example, if the input is 18, you should return
# [2,3,5,6,7,11,13,17]

# Hint: Exclude the multiples of primes.

# Given n, return all primes up to and including n.
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not. Intially, set each to true, expecting 0 and 1. 
    # Then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            #Sieve p's multiples.
            for i in range(p , n+1 , p):
                is_prime[i] = False
    return primes

# space complexity - O(n)
# time complexity - O(n^3/2/(logn)^2)



# Given n, return all primes up to and including n.
def generate_primes(n):
    if n < 2:
        return []
    size = (n-3) // 2+1 # size = ( (n - 3) // 2 ) + 1
    primes = [2] # stores the primes from 1 to n
    # is_prime[i] represents (2i +3) is prime or not.
    # Intially set each to true. Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index in is_prime
            # is (2i^2 + 6i +3) because is_prime[i] represents 2i+3.
            
            # notee that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i +3, size, p):
                is_prime[j] = False
    return primes

# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

# https://www.geeksforgeeks.org/sieve-of-eratosthenes/ 
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            print (p)
  
# driver program 
if __name__=='__main__': 
    n = 30
    print ("Following are the prime numbers smaller",) 
    print ("than or equal to", n)
    print(SieveOfEratosthenes(n))

Time complexity : O(n*log(log(n)))