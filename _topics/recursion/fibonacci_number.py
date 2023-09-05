# Fibonacci: Write a code to print Nth Fibonacci number

# Time: O(2^n) # exponential in nature
# Space: O(n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n = 10
    res = fibonacci(n)
    print(res)