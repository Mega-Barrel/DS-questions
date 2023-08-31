# Print n sum: Functional Approach

# Time: O(n)
# Space: O(n)

def printNSumFunctional(n):
    if n == 0:
        return 0
    return n + printNSumFunctional(n - 1)

n = 3
ret = printNSumFunctional(n=n)
print(ret)