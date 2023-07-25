import csv


from app.config import FILES_OUTPUT_DIR


def file_read(FILEPATH=FILES_OUTPUT_DIR.joinpath("people_data(extended).csv")):
    with open(FILEPATH) as csvfile:
        reader = list(csv.DictReader(csvfile))

        return reader


def show_information(file=None):
    if file is None:
        file = file_read()
    height_sum = 0
    weight_sum = 0
    for row in file:
        height_sum += float(row["Height(Inches)"])
        weight_sum += float(row["Weight(Pounds)"])

    average_height = height_sum / len(file) * 2.54
    average_weight = weight_sum / len(file) * 0.453592

    print("Ex #3")
    print(f"Average height = {average_height}\nAverage weight = {average_weight}")
