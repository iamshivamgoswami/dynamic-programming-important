class Solution:
    def isSubsequence(self, a: str, b: str) -> bool:
        left,right=0,0
        while left<len(a) and right<len(b):
            count=0
            if a[left]==b[right]:
                count+=1
                left+=1
                right+=1
            else:
                right+=1
        if count==len(a):
            return True
        return False

