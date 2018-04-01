import click
import time
from functools import wraps
from chess_square import (Square,
                          is_valid_square_name)


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


cli.add_command(colors)
cli.add_command(brothers)


if __name__ == "__main__":
    cli()