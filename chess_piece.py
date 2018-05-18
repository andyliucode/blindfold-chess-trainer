import string
import functools
from chess_square import (Square,
                          name_to_coord,
                          coord_to_name,
                          is_valid_square_coord,
                          is_valid_square_name)


# Note: if coords are numpy vectors then we wouldn't need this function
def coord_add(coordA, coordB):
    (x1, y1) = coordA
    (x2, y2) = coordB
    return (x1 + x2, y1 + y2)


def knight_moves(origin_square):
    """
    Takes an origin square and applies all possible knight-move vectors
    Square origin_square: the origin square
    returns filter-iterable: all legal squares reachable by a knight
    """
    origin = origin_square.coord
    add_to_origin = functools.partial(coord_add, origin)
    vectors = [(2, 1), (2, -1), (1, 2), (1, -2),
               (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

    heads = filter(is_valid_square_coord, map(add_to_origin, vectors))

    return heads
