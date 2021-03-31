#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

docker run --rm -p 5000:5000 -v $SCRIPT_DIR/sudoku:/tmp --name sudoku -it sudoku
