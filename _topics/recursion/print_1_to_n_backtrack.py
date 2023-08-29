# Print linearly, from 1 to n, using backtracking

# Time: O(n)
# Space: O(n)

def printNtimes(n):
    i = n
    def backtrack(i, n):
        if i < 1:
            print(f'executing if statement, value of i: {i}')
            return
        print(f'executing else statement, value of i: {i}')
        backtrack(i-1, n)
        print(i, end=' ')
    
    backtrack(i, n)

if __name__ == '__main__':
    n = int(input('Enter any N value: '))
    printNtimes(n)