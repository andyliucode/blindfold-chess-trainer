import click
import time
from chess_square import Square

@click.group()
def cli():
    pass

@click.command()
@click.argument('num', default=1)
def colors(num):
    white_names = {"White", "w", "W"}
    black_names = {"Black", "b", "B"}
    click.echo("Running drill with " + str(num) + " trials...")

    start_time = time.time()
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

    end_time = time.time()
    exit_msg = "\nNice job mate, you scored " + str(score) + '/' + str(num)
    time_taken = str(end_time - start_time) + "s"
    click.echo(exit_msg)
    click.echo(time_taken)

@click.command()
@click.argument('num', default=1)
def brothers(num):
    click.echo("Running drill with " + str(num) + " trials...")

    start_time = time.time()
    score = 0
    for x in range(num):
        square = Square.random()
        click.echo('\n')

        # while(input_square not in white_names.union(black_names)):
            # input_square = input("That's not a square, mate! Try again\n")

        brother_square = square.brother_square().name
        if (input_name == brother_square):
            click.echo("Correct!")
            score = score + 1
        else:
            response = "Incorrect, " + square.name + "'s brother' is " + brother_square
            click.echo(response)

    end_time = time.time()
    exit_msg = "\nNice job mate, you scored " + str(score) + '/' + str(num)
    time_taken = str(end_time - start_time) + "s"
    click.echo(exit_msg)
    click.echo(time_taken)

cli.add_command(colors)
cli.add_command(brothers)

if __name__ == "__main__":
    cli()