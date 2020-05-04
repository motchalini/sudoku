

class Sudoku:
    """ 数独ソルバー
    """

    def __init__(self):
        self.backtracks = 0


    def find_next_cell(self, grid):
        """ 次の空白セルを取得
        """
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    # 0 の座標を返す
                    return y, x
        # すべてのマスに数字が入っている状態
        return -1, -1


    def is_valid(self, grid, y, x, value):
        """ 有効チェック
        """
        # 行のチェック
        is_row = value not in grid[y]
        # 列のチェック
        is_column = value not in [i[x] for i in grid]
        # ブロックを取り出す
        blk_x, blk_y = (x//3) * 3, (y//3) * 3
        blk_grid = [i[blk_x:blk_x + 3] for i in grid[blk_y:blk_y + 3]]
        # ブロックのチェック
        is_block = value not in sum(blk_grid, [])
        # 有効チェック
        return all([is_row, is_column, is_block])
            

    def solve_sudoku(self, grid, y=0, x=0):
        """ ソルバー実行
        """
        y, x = self.find_next_cell(grid)
        # 終了判定
        if y == -1 or x == -1:
            return True
        # 入力
        for value in range(1, 10):
            if self.is_valid(grid, y, x, value):
                grid[y][x] = value
                # 次へ
                if self.solve_sudoku(grid, y, x):
                    return True
                # 巻き戻し
                self.backtracks += 1
                grid[y][x] = 0
        return False


if __name__ == '__main__':
    input_grid = [[0, 1, 8, 0, 0, 0, 3, 2, 0],
                  [2, 5, 0, 0, 0, 0, 0, 4, 6],
                  [0, 0, 4, 6, 5, 2, 1, 0, 0],
                  [0, 0, 6, 0, 7, 0, 2, 0, 0],
                  [0, 2, 0, 0, 4, 0, 0, 5, 0],
                  [0, 0, 3, 1, 0, 8, 7, 0, 0],
                  [0, 0, 2, 5, 3, 9, 4, 0, 0],
                  [4, 9, 0, 0, 0, 0, 0, 8, 3],
                  [0, 7, 0, 0, 0, 0, 0, 9, 0]]
    sudoku = Sudoku()
    print(sudoku.solve_sudoku(input_grid))
    print(sudoku.backtracks)
    [print(i) for i in input_grid]