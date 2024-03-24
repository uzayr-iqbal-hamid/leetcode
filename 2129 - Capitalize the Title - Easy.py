class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().split()
        ans = []
        for word in words:
            if len(word) <= 2:
                ans.append(word)
            else:
                ans.append(word.title())

        return " ".join(ans)
