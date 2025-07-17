class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num==".":
                    continue
                if num in row[i]:
                    return False
                row[i].add(num)
                if num in col[j]:
                    return False
                col[j].add(num)
                ind=(i//3)*3+j//3
                if num in box[ind]:
                    return False
                box[ind].add(num)
        return True