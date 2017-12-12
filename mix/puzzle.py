from copy import deepcopy
from trees.heap import Heap
from itertools import chain
from sys import maxsize


class PQ(Heap):

    def compare(self, a, b):
        return a[-1] < b[-1]


class Puzzle():

    def calc_goal_board(self, board):
        self.goal_board = sorted(chain.from_iterable(board),
                                 key=lambda x: x if x is not None else maxsize)

    def hamming(self, moves, board):
        cost = moves
        for x, y in zip(self.goal_board, chain.from_iterable(board)):
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
        i_size = len(board) - 1
        j_size = len(board[0]) - 1

        for i, j in [(i_empty - 1, j_empty),
                     (i_empty + 1, j_empty),
                     (i_empty, j_empty - 1),
                     (i_empty, j_empty + 1)]:
            if i > i_size or j > j_size:
                continue
            return_board = deepcopy(board)
            return_board[i][j], return_board[i_empty][j_empty] = return_board[i_empty][j_empty], return_board[i][j]
            yield return_board

    def solve(self, board):

        pq = PQ()
        moves = 0
        self.calc_goal_board(board)
        cost = self.hamming(moves, board)
        pq.insert(([board], cost))

        if cost == 0:
            return board, moves

        while not pq.is_empty():
            previous_boards, cost = pq.pop()
            last_board = previous_boards[-1]
            moves = len(previous_boards) - 1

            for board in self.possible_moves_gen(last_board):
                if board not in previous_boards:
                    new_previous_boards = deepcopy(previous_boards)
                    cost = self.hamming(moves, board)

                    # solution found
                    if cost - moves < 1:
                        new_previous_boards.append(board)
                        return new_previous_boards, moves

                    new_previous_boards.append(board)
                    pq.insert((new_previous_boards, cost))

    def to_str(self, board):
        result = ""
        cell_template = "%7s"
        for row in board:
            row_template = cell_template * len(row)
            row = row_template % tuple(row)
            result += row + "\n"
        return result


if __name__ == "__main__":
    initial_board = [[None,    1,        3],
                     [4,       2,        5],
                     [7,       8,        6]]
    puzzle = Puzzle()
    boards, _ = puzzle.solve(initial_board)
    for board in boards:
        print(puzzle.to_str(board))
