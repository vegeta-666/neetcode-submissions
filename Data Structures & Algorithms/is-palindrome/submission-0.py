import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumericSet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        left = 0
        right = len(s)-1

        while left < right:
            while (s[left] not in alphanumericSet and left < right):
                left +=1
            while (s[right] not in alphanumericSet and left < right):
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


