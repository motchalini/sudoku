import logging

logger = logging.getLogger(__name__)

MAX_BACKTRACKS = 10000


class Cell(object):
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Sudoku(object):

    def __init__(self):
        self.backtracks = 0

    def find_next_cell(self, grid: list) -> Cell:
        """ 次の空白セルを取得
        """
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    return Cell(y, x)
        return Cell(-1, -1)

    def is_valid(self, grid: list, cell: Cell, value: int) -> bool:
        """ 有効チェック
        """
        is_row = value not in grid[cell.y]

        is_column = value not in [i[cell.x] for i in grid]

        blk_x, blk_y = (cell.x//3) * 3, (cell.y//3) * 3
        blk_grid = [i[blk_x:blk_x + 3] for i in grid[blk_y:blk_y + 3]]
        is_block = value not in sum(blk_grid, [])

        return all([is_row, is_column, is_block])

    def get_solve_sudoku(
            self, grid: list, cell=Cell(0, 0), recursive=False) -> bool:
        """ ソルバー実行
        """
        if not recursive:
            logger.info('action=get_solve_sudoku status=run')
            self.backtracks = 0

        cell = self.find_next_cell(grid)

        if cell.y == -1 or cell.x == -1:
            return True

        for value in range(1, 10):
            if self.is_valid(grid, cell, value):
                grid[cell.y][cell.x] = value
                if self.get_solve_sudoku(grid, cell, recursive=True):
                    return True
                self.backtracks += 1
                if self.backtracks > MAX_BACKTRACKS:
                    return False
                grid[cell.y][cell.x] = 0
        return False
