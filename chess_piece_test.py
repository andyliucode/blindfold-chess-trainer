import unittest
from chess_square import (Square,
                          name_to_coord,
                          coord_to_name,
                          is_valid_square_coord,
                          is_valid_square_name)
from chess_piece import knight_moves


class TestChessPiece(unittest.TestCase):

    def setUp(self):
        self.top_left_corner = Square.from_coord((0,0))
        self.bot_right_corner = Square.from_coord((7,7))
        self.e4 = Square.from_name('e4')

    def test_knight_moves(self):
        moves = list(knight_moves(self.top_left_corner))
        self.assertEqual(moves, [(2,1), (1,2)])
        moves = list(knight_moves(self.bot_right_corner))
        self.assertEqual(moves, [(5,6), (6,5)])
        moves = list(knight_moves(self.e4))
        self.assertEqual(moves, [(6, 5), (6, 3), (5, 6), (5, 2), (2, 5), (2, 3), (3, 6), (3, 2)])


if __name__ == '__main__':
    unittest.main()