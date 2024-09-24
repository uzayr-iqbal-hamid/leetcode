class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        spl_chars = [" ", "!", "?", "'", ",", ";", "."]

        for i in spl_chars:
            paragraph = paragraph.replace(i, " ")

        words = paragraph.lower().split()

        count = {}

        for word in words:
            clean = word
            for i in word:
                if i in spl_chars:
                    clean = word.replace(i, "")
                else:
                    clean = word
            
            if clean not in banned:
                count[clean] = count.get(clean, 0) + 1


        res = max(zip(count.values(), count.keys()))[1]
        return res
