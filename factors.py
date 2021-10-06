def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results

# list comprehension
factors = [k for k in range(1, n+1) if n % k == 0]

# Using generators
def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k

# can now be used as
# for factor in factors(100)

# improvement on the factors program
# here we are only evaluating number up to the square root of that number
# while reporting factor n//k that is associated with each k(unless n//k equals k)

def factors(n):
    k = 1
    while k*k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:  # special case if n is a perfect square
        yield k