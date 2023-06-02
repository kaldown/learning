class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        indeces = []
        s = [i for i in s]
        for i, letter in enumerate(s):
            if letter.lower() in vowels:
                indeces.append((i, letter))
        i, j = 0, len(indeces) - 1
        while i <= j:
            li, ll = indeces[i]
            ri, rl = indeces[j]
            s[li] = rl
            s[ri] = ll
            i += 1
            j -= 1
        return ''.join(s)

