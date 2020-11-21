# Write a program that takes an integer argument and returns all the primes between 1 and that 
# integer. For example, if the input is 18, you should return
# [2,3,5,6,7,11,13,17]
n = 18
def generate_primes(n):
    if n < 2:
        return []
    size = (n-3) // 2+1
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
print(generate_primes(n))