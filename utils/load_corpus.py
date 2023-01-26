import pickle


def load_corpus(file_name="corpus.pkl"):
    file_path = f"./corpus/{file_name}"
    return pickle.load(open(file_path, "rb"))
