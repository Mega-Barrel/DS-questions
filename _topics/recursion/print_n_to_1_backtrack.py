# Print linearly, from n to 1, using backtracking

# Time: O(n)
# Space: O(n)

def printNtimes(n):
    i = 1
    def backtrack(i, n):
        if i > n:
            print(f'executing if statement, value of i: {i}')
            return
        print(f'executing else statement, value of i: {i}')
        backtrack(i+1, n)
        print(i, end=' ')
    
    backtrack(i, n)

if __name__ == '__main__':
    n = int(input('Enter any N value: '))
    printNtimes(n)