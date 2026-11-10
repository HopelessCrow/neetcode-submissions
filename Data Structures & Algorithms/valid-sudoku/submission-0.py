class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)

        row_list = [set() for _ in range(n)]
        column_list = [set() for _ in range(n)]
        grid_list = [set() for _ in range(n)]

        box_size = int(n ** 0.5)

        for i, row in enumerate(board):
            for j, val in enumerate(row):

                if val == ".":
                    continue

                # row check
                if val in row_list[i]:
                    return False
                row_list[i].add(val)

                # column check
                if val in column_list[j]:
                    return False
                column_list[j].add(val)

                # grid check
                grid_num = (i // box_size) * box_size + (j // box_size)

                if val in grid_list[grid_num]:
                    return False
                grid_list[grid_num].add(val)

        return True