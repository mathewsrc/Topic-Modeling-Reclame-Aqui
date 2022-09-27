from webscraping import execute
import click

@click.command()
@click.option('--input', type=click.File('r'), required=True, 
                prompt = 'Input file.txt',
                help='A file name to read names')
@click.option('--output', type=str, required=True, 
                prompt = 'Output file.txt',
                help='A file name to save results')
@click.option('--n', type=int, default=5, show_default=True,
                prompt='Enter the number of pages',
                help='The number of pages. Each page contains contains 1 or more complaints')
@click.option('--alert', type=bool,
                prompt='Show notification [y/N]',
                help='Show a notification on task finishes.')
def cli(input, output,  n, alert):
    execute(input, output, n, alert)


if __name__ =='__main__':
    cli()
