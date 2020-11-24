# Enumerate all primes to n

# A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.

# Write a program that takes an integer argument and returns all the primes between 1 and that 
# integer. For example, if the input is 18, you should return [2,3,5,6,7,11,13,17]

# Hint: Exclude the multiples of primes.

# Solution 1
# The natural brute-force algorithm is to iterate over all i from 2 to n, where n is the input to the program. For each i,
# we test if i is prime; if so we add it to the result. We can use "trial-division" to test if i is prime, i.e by dividing i 
# by each integer from 2 to the square root of i, and checking if the remainder is 0. (There is no need to test beyond the 
# square root of i, since if i has a divisor other than 1 and itself, it must also have a divisor that is no greater than its 
# square root.) Since, each test has time complexity O(√n), the time complexity of the entire computation is upper bounded by 
# O(n * √n). i.e, O(n^3/2)

# Intutively, the brute-force algorithm tests each number from 1 to n independently, and does not exploit the fact that we need
# to compute all primes from 1 to n. Heuristically, a better approach is to compute the primes and when a number is identified as
# as a prime, to "sieve" it, i.e, remove all its multiples from future consideration.
 
# Solution 2
# We use Boolean array to encode the candidates, i.e, if the ith entry in the array is true, then i is potentially a prime. Intially, 
# every number greater than or equal to 2 is a candidate. Whenver we determine a number is prime, we will add it to the result, which
# is an array. The first prime is 2. We add it to the result. None of it's multiples can be primes, so remove all its multiples from
# the candidate set by writing false in the corresponding locations. The next location set to true is 3. It must be a prime since nothing
# smaller than it and greater than 1 is a divisor of it. As before, we add it to result and remove its multiples from the candidate array.
# We continue till we get to the end of the array of candidates.

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

# We can improve runtime by sieving p's multiples from p^2 instead of p, since all members of the form kp, where k<p have
# already been sieved out. The storage can be reduced by ignoring even numbers.  

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

# The asymptotic time and space complexity are the same as that for the basic sieving approach.

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

# Time complexity : O(n*log(log(n)))