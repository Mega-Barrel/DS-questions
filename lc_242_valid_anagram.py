class Solution:
    # Time: O(n)
    # Space: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        res1 = self.checkAnagram(s)
        res2 = self.checkAnagram(t)

        return res1 == res2
    
    def checkAnagram(self, s):
        adict = {}

        for n in s:
            if n in adict:
                adict[n] += 1
            else:
                adict[n] = 1
        return adict

sol = Solution()
s = "rat"
t = "car"
res = sol.isAnagram(s, t)
print(res)