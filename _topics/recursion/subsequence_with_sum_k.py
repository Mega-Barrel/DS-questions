# Print all subsequence whose sum is K

# Time: O(2^n)
# Space: O(n)
def get_subsequence(arr, target):
    res = []
    
    def getSubSeq(n, curSum):
        if n >= len(arr):
            if curSum == target:
                print(res.copy())
            return
        
        curSum += arr[n]
        res.append(arr[n])
        getSubSeq(n+1, curSum)
        
        curSum -= arr[n]
        res.pop()
        getSubSeq(n+1, curSum)
    getSubSeq(0, 0)

if __name__ == '__main__':
    array = [1, 2, 1]
    target_sum = 2
    get_subsequence(arr=array, target=target_sum)

