# Print all subsequence: A contiguous/non contiguous sequence which follows the order.

# Time: O(2^n) # exponential in nature
# Space: O(n)

def sub_sequence(arr):
    output = []
    res = []
    
    def printSeq(n):
        if n >= len(arr):
            output.append(res.copy())
            return
        # Pick particular index into the subsequence
        res.append(arr[n])
        printSeq(n + 1)

        # Do not pick condition
        res.pop()
        printSeq(n + 1)

    printSeq(0)
    return output

if __name__ == '__main__':
    array = [3, 1, 2]
    res = sub_sequence(arr=array)
    print(res)