class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for sentence in sentences:
            maximum = max(len(sentence.split()), maximum)
        return maximum
