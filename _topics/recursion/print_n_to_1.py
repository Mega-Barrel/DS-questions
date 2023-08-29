# Print linearly, from n to 1

# Time: O(n)
# Space: O(n)
def printNtimes(count):

    def recursionPrint(cnt):
        if cnt < 1:
            return
        print(cnt, end=' ')
        recursionPrint(cnt-1)

    recursionPrint(count)

if __name__ == '__main__':
    n = int(input('Enter n value: '))
    printNtimes(n)