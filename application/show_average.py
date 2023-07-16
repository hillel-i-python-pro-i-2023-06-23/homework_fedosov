
import csv
from csv import DictReader
from typing import List, Any




def read_file(FILEPATH='people_data(extended).csv')-> list[Any]:
    with open(FILEPATH, 'r') as csvfile:
        reader = list(csv.DictReader(csvfile))

        return reader

def find_average_height(file=None)->float:
    if file is None:
        file = read_file()
    count = 0
    height_sum = 0
    for row in file:
        count += 1
        height_sum += float(row['Height(Inches)'])


    return height_sum / count * 2.54

def find_average_weight(file=None)->float:
    if file is None:
        file = read_file()
    count = 0
    weight_sum = 0
    for row in file:
        count += 1
        weight_sum += float(row['Weight(Pounds)'])

    return weight_sum / count * 0.453592


print(find_average_height())
print(find_average_weight())