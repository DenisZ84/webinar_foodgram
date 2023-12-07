import csv
from django.conf import settings

CSV_PATH = f'{settings.MEDIA_ROOT}/eggs.csv'

def create_csv():
    with open(CSV_PATH, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def open_csv():
    with open(CSV_PATH, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            print(', '.join(row))