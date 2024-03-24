class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = ""
        for i in digits:
            string += str(i)

        increment = int(string) + 1

        new_list = list(str(increment))

        ans = [int(i) for i in new_list]
        return ans
