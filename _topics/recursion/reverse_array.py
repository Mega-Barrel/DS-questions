# reverse array:

# Time: O(n)
# Space: O(n)
def reverse_recurssion(arr):
    res = []
    i = 0

    def recurssion(arr, i):
        if i > len(arr) - 1:
            return
        recurssion(arr, i+1)
        res.append(arr[i])

    recurssion(arr, i)
    return res

# Time: O(n/2)
# Space: O(n)
def reverse_swap(arr, i, n):
    if i >= len(arr)/2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse_swap(arr, i+1, n)

if __name__ == '__main__':
    array = [ 1, 2, 3, 4, 2 ]
    n = len(array)

    # With extra space
    res = reverse_recurssion(arr=array)
    print(res)

    # Inplace array
    reverse_swap(array, 0, n)
    print(array)