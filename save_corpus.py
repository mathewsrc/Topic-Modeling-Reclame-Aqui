import pickle
import os
import click

def save_corpus(corpus, option):
  prep_file_path = '/content/Topic-Modeling-Reclame-Aqui/corpus/preprocessed'
  raw_file_path = '/content/Topic-Modeling-Reclame-Aqui/corpus/raw'

  if option == 'raw':
    if not os.path.exists(raw_file_path):
      os.makedirs(raw_file_path)
    pickle.dump(corpus, open('%s/corpus.p' %raw_file_path, 'wb'))
    print(f"Corpus saved to {raw_file_path}")
  elif option == 'preprocessed':
    if not os.path.exists(prep_file_path):
      os.makedirs(prep_file_path)
    pickle.dump(corpus, open('%s/corpus.p' %prep_file_path, 'wb'))
    print(f"Corpus saved to {prep_file_path}")


@click.command()
@click.option('--corpus', required=True)
@click.option('--option', type=click.Choice(['raw', 'preprocessed']), required=True, prompt="Select one option:")
def cli(corpus, option):
  save_corpus(corpus, option)


if __name__ =='__main__':
    cli()
