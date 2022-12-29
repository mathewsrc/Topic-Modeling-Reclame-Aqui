import pickle
import os


def save_corpus(corpus, file_name="corpus.pkl"):
    file_path = f"./corpus/{file_name}"

    if not os.path.exists("./corpus"):
        os.makedirs("./corpus")
    with open(file_path, "wb") as f:
        # Save the DataFrame to the file
        pickle.dump(corpus, f)
