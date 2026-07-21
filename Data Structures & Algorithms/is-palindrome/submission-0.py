class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tmp = "".join(ch for ch in s if ch.isalnum())
        return tmp==tmp[::-1]