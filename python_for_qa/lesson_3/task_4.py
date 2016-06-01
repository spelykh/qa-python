__author__ = 'Stepan_Pelykh'

import csv

data = []


def decrease_priority(filename, param):
    reader = csv.DictReader(filename, delimiter=',')

    for row in reader:
        try:
            if row[param] == 'critical':
                row[param] = 'high'
                data.append(row)
            elif row[param] == 'high':
                row[param] = 'medium'
                data.append(row)
            elif row[param] == 'medium':
                row[param] = 'low'
                data.append(row)
        except IndexError as e:
            print(e)
            pass


def changing(input_file, output_file):

    with open(input_file, 'r') as in_file:
        decrease_priority(in_file, 'Priority')

        with open(output_file, 'w') as out_file:
            header = ['#', 'Description', 'Environment', 'Priority', 'Owner', 'Created At']
            writer = csv.DictWriter(out_file, fieldnames=header)

            writer.writeheader()
            writer.writerows(data)

changing('Python for QA - bugs list - Sheet1.csv', 'new_bug_list.csv')

