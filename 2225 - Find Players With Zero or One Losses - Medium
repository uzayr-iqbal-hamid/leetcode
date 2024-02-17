class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        lost = {}

        for winner, loser in matches:
            lost[winner] = lost.get(winner, 0)
            lost[loser] = lost.get(loser, 0) + 1

        always_won = []
        lost_one = []

        for player, loss in lost.items():
            if loss == 0:
                always_won.append(player)
            if loss == 1:
                lost_one.append(player)

        return [sorted(always_won), sorted(lost_one)]
