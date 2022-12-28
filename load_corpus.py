import pickle
import os
import click

def load_corpus(option, ):
  prep_file_path = '/content/Topic-Modeling-Reclame-Aqui/corpus/preprocessed'
  raw_file_path = '/content/Topic-Modeling-Reclame-Aqui/corpus/raw'

  if option == 'raw':
    return pickle.load(open('%s/corpus.p' %raw_file_path, 'rb'))
  elif option == 'preprocessed':
    return pickle.load(open('%s/corpus.p' %prep_file_path, 'rb'))

@click.command()
@click.option('--option', type=click.Choice(['raw', 'preprocessed']), prompt="Select one option:")
def cli(option):
  print("Data loaded to variable name: corpuss")
  return load_corpus(option)

if __name__ == '__main__':
  corpuss = cli()
