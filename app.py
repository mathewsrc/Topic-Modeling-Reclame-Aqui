from webscraping import execute
import click

@click.command()
@click.option('--name', type=str, required=True, 
                prompt = 'Please enter a company name',
                help='The company name you are look for')
@click.option('--n', type=int, default=100, show_default=True,
                prompt='Enter the number of items to collect default is',
                help='The number of items to collect.')
def cli(name, n):
    execute(name, n)


if __name__ =='__main__':
    cli()
