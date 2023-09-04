# Check if string is palindrome or not

# Time: O(n/2)
# Space: O(n)

def is_palindrome(string, i, n):
    if i >= n/2:
        return True
    if string[i] != string[n - i - 1]:
        return False
    return is_palindrome(string, i+1, n)

if __name__ == '__main__':
    string = 'madam'
    i = 0
    n = len(string)
    res = is_palindrome(string, i, n)
    print(res)
