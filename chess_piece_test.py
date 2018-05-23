import unittest
from chess_square import name_to_coord
from chess_piece import (knight_moves,
                         shortest_path)
from collections import deque


class TestChessPiece(unittest.TestCase):

    def setUp(self):
        self.top_left_corner = (0,0)
        self.bot_right_corner = (7,7)
        self.e4 = name_to_coord('e4')

    def test_knight_moves(self):
        moves = list(knight_moves(self.top_left_corner))
        self.assertEqual(moves, [(2,1), (1,2)])
        moves = list(knight_moves(self.bot_right_corner))
        self.assertEqual(moves, [(5,6), (6,5)])
        moves = list(knight_moves(self.e4))
        self.assertEqual(moves, [(6, 5), (6, 3), (5, 6), (5, 2), (2, 5), (2, 3), (3, 6), (3, 2)])

    def test_shortest_path(self):
        self.assertEqual(shortest_path((0,0), (2,1), knight_moves), (1, deque([(0,0), (2,1)])))
        self.assertEqual(shortest_path((0,0), (4,2), knight_moves), (2, deque([(0, 0), (2, 1), (4, 2)])))
        self.assertEqual(shortest_path((0,0), (3,4), knight_moves), (3, deque([(0, 0), (2, 1), (4, 2), (3, 4)])))

if __name__ == '__main__':
    unittest.main()