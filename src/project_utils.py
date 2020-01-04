import string
import csv


def remove_punctuation(my_str):
    clean_str = my_str.translate(str.maketrans('', '', string.punctuation))
    return clean_str


def dict_to_file(my_dict, output_file, delimiter=','):
    with open(output_file, 'w') as f_output:
        writer = csv.writer(f_output, delimiter=delimiter)
        for key, value in my_dict.items():
            writer.writerow([key, value])

