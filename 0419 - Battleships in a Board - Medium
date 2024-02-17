class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        battle_ships_cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                battle_ships_cnt += int(board[i][j] == "X" and (i == 0 or board[i - 1][j] != "X") and (j == 0 or board[i][j - 1] != "X"))
        
        return battle_ships_cnt
