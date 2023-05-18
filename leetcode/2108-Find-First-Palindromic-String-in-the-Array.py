class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s):
            middle = len(s) // 2
            return s[:middle][::-1] == s[middle + (1 if len(s) % 2 else 0):]
        
        for word in words:
            if is_palindrome(word):
                return word
        else:
            return ""
