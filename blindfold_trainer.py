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
	for x in xrange(num):
		square = Square.random()
		click.echo('\n')
		input_color = raw_input(square.name + '\n')

		while(input_color not in white_names.union(black_names)):
			input_color = raw_input("That's not a color, mate! Try again\n")

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

cli.add_command(colors)

if __name__ == "__main__":
	cli()