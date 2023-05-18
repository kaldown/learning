class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        def find_longest(word):
            letters = set()
            i = 0
            for letter in word:
                if letter in letters:
                    return i
                letters.add(letter)
                i += 1
            return i

        longest = 0
        i = 0
        while i < len(s):
            curr_longest = find_longest(s[i:])
            longest = max(longest, curr_longest)
            i += 1
        return longest

