import csv
from pythomon import Pythomon


def createpythomons():
    # https://stackoverflow.com/questions/40077694/how-do-i-import-a-csv-into-an-have-each-line-be-an-object
    # shout to this guy^ for the help
    # Read values from csv file.
    values = []
    with open('pythomons.csv', 'r') as csv_file:
        # Replace the delimiter with the one used in your CSV file.
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row_values in csv_reader:
            # If a line in your CSV file looks like this: a,b,c
            # Then row_values looks something like this: ['a', 'b', 'c']
            values.append(row_values)

    # Convert the list of lists (which represent the CSV values) to objects.
    column_names = ['idnum', 'name', 'form', 'type1', 'type2', 'total', 'hp', 'atk', 'defn', 'spatk', 'spdef', 'spd',
                    'gen']
    pythomons = []
    for row_values in values:
        pythomons.append({key: value for key, value in zip(column_names, row_values)})

    # pythomons is now a list of dicts with one dict per line of the CSV file.
    # The dicts could e.g. be converted to objects with this:
    pythomonobjects = [Pythomon(**pythomon) for pythomon in pythomons]

    class pythomonPackage:
        def __init__(self):
            self.pythomonobjects = pythomonobjects
            self.pythomonslist = pythomons

    pytho = pythomonPackage()
    return pytho

