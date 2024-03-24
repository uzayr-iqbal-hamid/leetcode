class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest_word = ''

        for word in dictionary:
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
            if i == len(word):
                if len(word) > len(longest_word) or len(word) == len(longest_word) and word < longest_word:
                    longest_word = word

        return longest_word  
