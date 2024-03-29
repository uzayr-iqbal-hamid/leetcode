class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        find = collections.defaultdict(list)
        def toMinutes(time):
            return int(time[:2]) * 60 + int(time[2:])

        for employee, time in access_times:
            find[employee].append(toMinutes(time))

        high_access = []
        for name in find:
            find[name].sort()

            dQ = collections.deque()
            for allTimes in find[name]:
                dQ.append(allTimes)

                while dQ[-1] - dQ[0] >= 60:
                    dQ.popleft()
                
                if len(dQ) >= 3:
                    high_access.append(name)

        return high_access
