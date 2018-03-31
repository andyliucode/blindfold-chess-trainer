from chess_square import (Square,
						  name_to_coord,
						  coord_to_name)

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

	

if __name__ == '__main__':
	main() 