import click
import time
from functools import wraps
from chess_square import (Square,
                          coord_to_name,
                          name_to_coord,
                          is_valid_square_name)
from chess_piece import (knight_moves,
                         find_shortest_path,
                         is_legal_path)

def reporter(func):
    @wraps(func)
    def wrapper(num):
        click.echo("Running drill with " + str(num) + " trials...")
        start_time = time.time()
        
        score = func(num)

        end_time = time.time()
        exit_msg = "\nNice job mate, you scored " + str(score) + '/' + str(num)
        time_taken = str(end_time - start_time) + "s"
        click.echo(exit_msg)
        click.echo(time_taken)
    return wrapper


@click.group()
def cli():
    pass


@click.command()
@click.argument('num', default=1)
@reporter
def colors(num):
    white_names = {"White", "w", "W"}
    black_names = {"Black", "b", "B"}

    score = 0
    for x in range(num):
        square = Square.random()
        click.echo('\n')
        input_color = input(square.name + '\n')

        while(input_color not in white_names.union(black_names)):
            input_color = input("That's not a color, mate! Try again\n")

        correct_names = white_names if square.color() == "White" else black_names
        if (input_color in correct_names):
            click.echo("Correct!")
            score = score + 1
        else:
            response = "Incorrect, " + square.name + " is " + square.color()
            click.echo(response)
    return score


@click.command()
@click.argument('num', default=1)
@reporter
def brothers(num):
    """
    Reflects the square across the a1-h8 diagonal. The brother square is in the same relative location if you rotated the board 180 degrees. 
    """
    score = 0
    for x in range(num):
        square = Square.random()
        click.echo('\n')
        input_name = input(square.name + '\n')

        while(not is_valid_square_name(input_name)):
            input_name = input("That's not a square, mate! Try again\n")

        brother_square = square.brother_square().name
        if (input_name == brother_square):
            click.echo("Correct!")
            score = score + 1
        else:
            response = "Incorrect, " + square.name + "'s brother is " + brother_square
            click.echo(response)
    return score


@click.command()
@click.argument('num', default=1)
@reporter
def knight_path(num):
    """
    Finds the shortest path between two squares, one on the first rank and one on the 
    eighth rank. 
    """
    score = 0
    for x in range(num):
        # REQUIRES: starting_square != target_square
        starting_square = Square.random_inside((7,0), (7,7))
        target_square = Square.random_inside((0,0), (0,7))
        click.echo('\n')
        shortest_path = find_shortest_path(starting_square.coord, target_square.coord, knight_moves)
        num_moves = len(shortest_path) - 1
        
        input_len = input(starting_square.name + " to " + target_square.name + '\n')

        def bad_response():
            return "Incorrect, " + target_square.name + " can be reached in " + str(num_moves) + " moves, e.g." + '\n' + ' '.join(list(map(coord_to_name, shortest_path)))

        if (int(input_len) == num_moves):
            def process_path(input_path):
                path = input_path.split(' ')

                # Need to prepend the starting square if it was missing due to 
                # is_legal_path's contract
                if (path[0] != starting_square.name):
                    path = [starting_square.name] + path

                return path

            path = process_path(input("Yes, please give a path:\n"))
            while (len(path) != num_moves + 1):
                path = process_path(input("Sorry, path length was incorrect. Try again:\n"))

            # Converts all square names in the path to coordinates and checks if the path is a legal path from starting_square to target_square
            if is_legal_path(starting_square.coord, target_square.coord, knight_moves, list(map(lambda x: name_to_coord(x),path))):
                click.echo("Correct!")
                score = score + 1
            else:
                click.echo(bad_response())
        else:
            click.echo(bad_response())

    return score


cli.add_command(colors)
cli.add_command(brothers)
cli.add_command(knight_path)


if __name__ == "__main__":
    cli()