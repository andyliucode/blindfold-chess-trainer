import string
from random import randint


def name_to_coord(name):
    """
    Takes a square name and converts it to 2d-array coordinates, e.g. 'a8' to (0,0) and 'h4' to (4,7)

    string name: the name of a square, e.g. 'a1' or 'e4'
    returns int, int: 2d-array integer coordinates
    """
    rank_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    ffile, rank = name[0], int(name[1])
    
    row = 8 - rank
    col = rank_to_num[ffile]

    return (row, col)


def coord_to_name(coord):
    """
    Takes a 2d-array coordinate and converts it to a chess board square name, e.g. (0,0) to 'a8' and (4,7) to 'h4'

    int row: value between 0 and 7
    int col: value between 0 and 7 
    returns string name: the name of a square, e.g. 'a1' or 'e4' 
    """
    (row, col) = coord
    num_to_rank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rank = str(8 - row)
    ffile = num_to_rank[col]

    return ffile + rank


def is_valid_square_coord(coord):
    (row, col) = coord
    valid_row = (0 <= row) and (row <= 7)
    valid_col = (0 <= col) and (col <= 7)
    return valid_row and valid_col


def is_valid_square_name(name):
    if len(name) != 2:
        return False
    if name[0] not in ['abcdefgh']:
        return False
        
    coord = coord_to_name(name)
    return is_valid_square_coord(coord)


class Square:
    """
    Represents a square on a chess board, an 8x8 grid of squares where odd parity squares are white and even parity squares are black. 

    (int, int) coord: a tuple representing a 2d-array coordinate
    string name: the algebraic name of the square
    """

    def __init__(self, coord, name):
        assert(name_to_coord(name) == coord)
        self.coord = coord
        self.name = name

    @classmethod
    def from_name(cls, name):
        coord = name_to_coord(name)
        return cls(coord=coord, name=name)

    @classmethod
    def from_coord(cls, coord):
        name = coord_to_name(coord)
        return cls(coord=coord, name=name)

    @classmethod
    def random(cls):
        rand_coord = (randint(0,7), randint(0,7))
        rand_square = coord_to_name(rand_coord)
        return cls(coord=rand_coord, name=rand_square)

    def color(self):
        (row, col) = self.coord
        parity_of_coord = (row + col) % 2
        color = ("Black" if parity_of_coord else "White")
        return color

    def brother_square(self):
        """
        Reflects the square across the a1-h8 diagonal. The brother square is in the 
            same relative location if you rotated the board 180 degrees. 
        """
        (row, col) = self.coord
        new_coord = (7 - row, 7 - col)
        return Square.from_coord(new_coord)