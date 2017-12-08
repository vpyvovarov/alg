from copy import deepcopy
from trees.heap import Heap
from itertools import chain
from pprint import pprint, pformat
from sys import maxsize

class PQ(Heap):

    def compare(self, a, b):
        return a[-1] < b[-1]

class Puzzle():

    def __init__(self, board):
        self.board = deepcopy(board)
        self.goal_board = sorted(chain.from_iterable(self.board),
                                 key=lambda x: x if x is not None else maxsize)
        
    def hamming(self, moves, board):
        cost = moves
        for x, y in  zip(self.goal_board, chain.from_iterable(board)):
            if x != y:
                cost += 1
        return cost
    
    def _find_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is None:
                    return i, j

    def possible_moves_gen(self, board):
        i_empty, j_empty = self._find_empty(board)
        for i, j in [(i_empty - 1, j_empty),
                     (i_empty + 1, j_empty),
                     (i_empty, j_empty - 1),
                     (i_empty, j_empty + 1)]:
            try:
                return_board = deepcopy(board)
                return_board[i][j], return_board[i_empty][j_empty] = return_board[i_empty][j_empty], return_board[i][j]
            except IndexError:
                continue
            yield return_board

    def solve(self):
        self.pq = PQ()
        moves = 0
        discovered =[self.board]
        cost = self.hamming(moves, self.board)
        self.pq.insert((self.board, moves, cost))
        while not self.pq.is_empty():
            previous_board, moves, cost = self.pq.pop()
            print("cost = %s, moves = %s, q_size=%s" % (cost-moves, moves, self.pq.size()))
            if cost - moves < 1:
                return previous_board, moves
            for board in self.possible_moves_gen(previous_board):
                if board not in discovered:
                    # print('-----')
                    cost = self.hamming(moves, board) 
                    self.pq.insert((board, moves + 1, cost))
        
    
    def __str__(self):
        result = ""
        cell_template = "%7s"
        for row in self.board:
            row_template = cell_template * len(row)
            row = row_template % tuple(row)
            result += row + "\n"
        return result

if __name__ == "__main__":
    initial_board = [[None,    1,        3],
                     [4,       2,        6],
                     [7,       5,        8]]
    # initial_board = [[1,       3,        5],
    #                  [6,    None,        4],
    #                  [2,       8,        7]]
    puzzle = Puzzle(initial_board)
    result = puzzle.solve()
    print(result)
    # boards = []
    # for board in puzzle.possible_moves_gen(initial_board):
    #     boards.append(board)
    # for board in boards:
    #     puzzle.board = board
    #     print(puzzle)
    #     print(puzzle.hamming(0, board))