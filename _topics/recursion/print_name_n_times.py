# Print names n times

# Time: O(n)
# Space: O(n)
def printNtimes(s):
    count = 0

    def recursionPrint(cnt):
        if cnt == 5:
            return
        print(s)
        recursionPrint(cnt+1)

    recursionPrint(count)

if __name__ == '__main__':
    printNtimes('Data Analyst!')