# Print n sum: Parameterized Approach

# Time: O(n)
# Space: O(n)

def printNSum(n, cursum):
    if n < 1:
        print(cursum)
        return
    cursum += n
    printNSum(n - 1, cursum)

n = 5
cursum = 0
printNSum(n=n, cursum=cursum)