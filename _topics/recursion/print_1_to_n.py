# Print linearly, from 1 to n

# Time: O(n)
# Space: O(n)
def printNtimes():
    count = 1

    def recursionPrint(cnt):
        if cnt == 11:
            return
        print(cnt, end=' ')
        recursionPrint(cnt+1)

    recursionPrint(count)

if __name__ == '__main__':
    printNtimes()