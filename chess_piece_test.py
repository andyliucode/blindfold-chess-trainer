import unittest
from chess_square import name_to_coord
from chess_piece import (knight_moves,
                         find_shortest_path,
                         is_legal_path)
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

    def test_find_shortest_path(self):
        self.assertEqual(find_shortest_path((0,0), (2,1), knight_moves), [(0,0), (2,1)])
        self.assertEqual(find_shortest_path((0,0), (4,2), knight_moves), [(0, 0), (2, 1), (4, 2)])
        self.assertEqual(find_shortest_path((0,0), (3,4), knight_moves), [(0, 0), (2, 1), (4, 2), (3, 4)])

    def test_is_legal_path(self):
        self.assertTrue(is_legal_path((0,0), (2,1), knight_moves, [(0,0), (2,1)]))
        self.assertTrue(is_legal_path((0,0), (4,2), knight_moves, [(0,0), (2,1), (4,2)]))
        self.assertTrue(is_legal_path((0,0), (3,4), knight_moves, [(0,0), (2,1), (4,2), (3,4)]))

    def test_is_legal_shortest_path(self):
        self.assertTrue(is_legal_path((0,0), (3,4), knight_moves, find_shortest_path((0,0), (3,4), knight_moves)))
        self.assertFalse(is_legal_path((1,1), (3,4), knight_moves, find_shortest_path((0,0), (3,4), knight_moves)))
        self.assertFalse(is_legal_path((0,0), (4,4), knight_moves, find_shortest_path((0,0), (3,4), knight_moves)))
        self.assertFalse(is_legal_path((0,0), (3,4), knight_moves, []))

if __name__ == '__main__':
    unittest.main()