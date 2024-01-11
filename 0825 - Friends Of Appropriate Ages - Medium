class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def isRequestPossible(a, b):
            if (b <= 0.5 * a + 7) or (b > a):
                return False
            return True

        age_group = collections.Counter(ages)
        request_count = 0
        for a, numOf_a in age_group.items():
            for b, numOf_b in age_group.items():
                if isRequestPossible(a, b):
                    request_count += numOf_a * numOf_b
                    if a == b:
                        request_count -= numOf_a
        return request_count
