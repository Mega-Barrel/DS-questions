# Print n sum: Functional Approach

# Time: O(n)
# Space: O(n)

def factorialFunctional(n):
    if n == 1:
        return 1
    return n * factorialFunctional(n - 1)

n = 5
res = factorialFunctional(n=n)
print(res)