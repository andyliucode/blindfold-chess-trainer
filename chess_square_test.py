from chess_square import (Square,
                          name_to_coord,
                          coord_to_name,
                          is_valid_square_coord,
                          is_valid_square_name)


def main():
    # Test name_to_coord
    assert(name_to_coord('a8') == (0,0))
    assert(name_to_coord('a1') == (7,0))
    assert(name_to_coord('h8') == (0,7))
    assert(name_to_coord('h1') == (7,7))
    assert(name_to_coord('e4') == (4,4))
    assert(name_to_coord('h4') == (4,7))

    # Test coord_to_name
    assert(name_to_coord(coord_to_name((0,0))) == (0,0))
    assert(name_to_coord(coord_to_name((7,0))) == (7,0))
    assert(name_to_coord(coord_to_name((0,7))) == (0,7))
    assert(name_to_coord(coord_to_name((7,7))) == (7,7))

    # Test from_name
    square_from_name = Square.from_name('e4')
    assert(square_from_name.name == 'e4')
    assert(square_from_name.coord == (4,4))

    # Test from_coord
    square_from_coord = Square.from_coord((4,4))
    assert(square_from_coord.name == 'e4')
    assert(square_from_coord.coord == (4,4))

    # Test color_of_square
    assert(Square.from_name('a8').color() == 'White')
    assert(Square.from_name('a1').color() == 'Black')
    assert(Square.from_name('h1').color() == 'White')
    assert(Square.from_name('h8').color() == 'Black')

    # Test brother_square
    assert(Square.from_name('a8').brother_square().name == 'h1')
    assert(Square.from_name('c4').brother_square().name == 'f5')
    assert(Square.from_name('e1').brother_square().name == 'd8')
    assert(Square.from_name('d4').brother_square().name == 'e5')

    # Test is_valid_square_coord
    assert(is_valid_square_coord((0,7)))
    assert(is_valid_square_coord((7,0)))
    assert(not is_valid_square_coord((-1,0)))
    assert(not is_valid_square_coord((0,-1)))
    assert(not is_valid_square_coord((8,0)))
    assert(not is_valid_square_coord((0,8)))

    # Test is_valid_square_name
    assert(is_valid_square_name('a1'))
    assert(is_valid_square_name('h8'))
    assert(is_valid_square_name('e4'))
    assert(not is_valid_square_name('E4'))
    assert(not is_valid_square_name('h10'))
    assert(not is_valid_square_name('i1'))


if __name__ == '__main__':
    main() 