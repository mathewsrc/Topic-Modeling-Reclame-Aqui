from email.policy import default
from webscraping import execute
import click

@click.command()
@click.option('--input', type=click.File('r'), required=True)
@click.option('--output', type=str, required=True)
@click.option('--n', type=int, default=5, show_default=True,
                prompt='Enter the number of pages',
                help='The number of pages. Each page contains contains 1 or more complaints')
@click.option('--start_from', type=int, default=0,
              prompt='Select the start page to collect from',
              help='Select the page position to start collect data')
@click.option('--alert', type=bool, default='y',
                prompt='Show notification [y/N]',
                help='Show a notification on task finishes.')
def cli(input, output,   n, start_from, alert):
    execute(input, output,  n, start_from,  alert)


if __name__ =='__main__':
    cli()
