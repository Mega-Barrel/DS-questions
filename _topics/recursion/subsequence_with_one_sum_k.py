# Print all subsequence whose sum is K, and print only 1 sequence

# Time: O(2^n)
# Space: O(n)
def get_1_subsequence(arr, target):
    res = []
    
    def _getSubSeq(n, curSum):
        if n >= len(arr):
            if curSum == target:
                print(res.copy())
                return True
            else:
                return False
        
        curSum += arr[n]
        res.append(arr[n])
        if (_getSubSeq(n+1, curSum) == True):
            return True

        curSum -= arr[n]
        res.pop()
        if (_getSubSeq(n+1, curSum) == True):
            return True
        return False
    _getSubSeq(0, 0)

if __name__ == '__main__':
    array = [1, 2, 1]
    target_sum = 2
    get_1_subsequence(arr=array, target=target_sum)
