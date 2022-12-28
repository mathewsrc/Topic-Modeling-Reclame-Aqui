import pickle
import os

def load_corpus(option='preprocessed'):
  prep_file_path = '/content/Topic-Modeling-Reclame-Aqui/corpus/preprocessed'
  raw_file_path = '/content/Topic-Modeling-Reclame-Aqui/corpus/raw'

  if option == 'raw':
    return pickle.load(open('%s/corpus.p' %raw_file_path, 'rb'))
  elif option == 'preprocessed':
    return pickle.load(open('%s/corpus.p' %prep_file_path, 'rb'))
