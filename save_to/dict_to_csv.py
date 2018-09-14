import csv


def save_to_csv(info):
    with open('hello-github.csv', 'a', encoding='utf-8') as csvfile:
        fieldnames = ['aaa', 'bbb', 'ccc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(info)