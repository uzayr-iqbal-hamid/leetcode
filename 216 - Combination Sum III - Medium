class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        outer = []

        def Combiner(k: int, n: int, s: int, path: List[int]) -> None:
            if k == 0 and n == 0:
                outer.append(path)
                return
            if k == 0 or n < 0:
                return

            for i in range(s, 10):
                Combiner(k - 1, n - i, i + 1, path + [i])

        
        Combiner(k, n, 1, [])
        return outer
