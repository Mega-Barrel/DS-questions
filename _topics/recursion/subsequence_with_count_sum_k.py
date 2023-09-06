# count all subsequence whose sum is K

# Time: O(2^n)
# Space: O(n)

def count_subsequence(arr, k):
    res = []
    count = 0

    def getCount(n, curSum):
        nonlocal count
        if n >= len(arr):
            if curSum == k:
                count += 1
            return

        # Take
        curSum += arr[n]
        res.append(arr[n])
        getCount(n+1, curSum)

        # not Take
        curSum -= arr[n]
        res.pop()
        getCount(n+1, curSum)

    getCount(0, 0)
    return count

if __name__ == '__main__':
    array = [1, 2, 1]
    target = 2
    res = count_subsequence(arr=array, k=target)
    print(res)