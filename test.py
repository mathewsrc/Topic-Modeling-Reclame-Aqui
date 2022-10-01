
import csv

with open('corpus.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        csv_headings = next(reader)
        print('title' not in csv_headings[0])