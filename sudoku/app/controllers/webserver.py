from copy import deepcopy
import logging

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from solver.solver import Sudoku

logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='../views')
sudoku = Sudoku()


@app.route('/')
def index():
    return render_template('sudoku.html')


@app.route('/api/result/', methods=['POST'])
def api_result():
    values = request.values
    y_list = []
    for y in range(0, 9):
        x_list = []
        for x in range(0, 9):
            try:
                cell_value = int(values['cell{}{}'.format(y, x)])
            except ValueError:
                cell_value = 0
            x_list.append(cell_value)
        y_list.append(x_list)

    sudoku_list = deepcopy(y_list)
    if sudoku.get_solve_sudoku(sudoku_list):
        logger.info(f'action=api_result backtracks={sudoku.backtracks}')
        return jsonify(
            {'backtracks': sudoku.backtracks, 'values': sudoku_list}), 200
    else:
        logger.warning('action=api_result error=backtracks_upper_limit_over')
        return jsonify({'message': 'backtracks upper limit over'}), 400


def start():
    app.debug = True
    app.run(host='0.0.0.0')
