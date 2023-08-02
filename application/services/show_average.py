
import csv

from application.config import FILES_OUTPUT_DIR



def file_read(file_path=None):
    if file_path is None:
        file_path = FILES_OUTPUT_DIR.joinpath('people_data(extended).csv')
    with open(file_path, 'r') as csvfile:
        reader = list(csv.DictReader(csvfile))

        return reader

def find_average_height(csv_file=None)->float:
    if csv_file is None:
        csv_file = file_read()
    height_sum = 0

    for row in csv_file:
        height_sum += float(row['Height(Inches)'])


    return height_sum / len(csv_file)



def find_average_weight(csv_file=None)->float:
    if csv_file is None:
        csv_file = file_read()
    weight_sum = 0

    for row in csv_file:
        weight_sum += float(row['Weight(Pounds)'])

    return weight_sum / len(csv_file)

def convert_weight(weight:float = find_average_weight())->float:
    return weight  * 0.453592


def convert_height(height:float = find_average_height())->float:
    return height * 2.54



def show_information(height:float = convert_height(), weight:float = convert_weight()):
    return f"<b>Average height{height};<br>Average weight{weight}</b>"
