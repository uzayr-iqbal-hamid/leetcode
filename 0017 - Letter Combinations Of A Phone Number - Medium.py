class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = { 
        "2": "abc", 
        "3": "def", 
        "4": "ghi", 
        "5": "jkl",
        "6": "mno", 
        "7": "pqrs", 
        "8": "tuv", 
        "9": "wxyz"
        }

        if digits == "":
            return []

        letters = list(map[digits[0]])

        for digit in digits[1:]:
            letters = [old+new for old in letters for new in list(map[digit])]

        return letters
