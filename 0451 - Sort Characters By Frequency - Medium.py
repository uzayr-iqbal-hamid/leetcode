class Solution:
    def frequencySort(self, s: str) -> str:      
        frequency = collections.Counter(s)
        sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        result = []

        for char, freq in sorted_chars:
            result.append(char * freq)

        return ''.join(result)
