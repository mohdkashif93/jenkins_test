from _collections import defaultdict
from src.project_utils import dict_to_file, remove_punctuation


def get_word_count(input_filename):
    with open(input_filename) as f_input:
        lines = f_input.readlines()
        word_dict = defaultdict(int)
        for line in lines:
            clean_line = remove_punctuation(line)
            for word in clean_line.split(' '):
                word_dict[word] += 1
    return word_dict


if __name__ == "__main__":
    inp_filename = 'sample.txt'
    out_filename = 'count.csv'
    print("Reading file ", inp_filename)
    word_dict = get_word_count(inp_filename)
    print("Output from get_word_count is")
    print(word_dict)
    print("Writing to file named", out_filename)
    dict_to_file(word_dict, out_filename)
