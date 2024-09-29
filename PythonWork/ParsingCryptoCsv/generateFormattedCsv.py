import csv
import os
import re

def main():
    try:
        current_dir = os.getcwd()
        input_csv_name = "BTC_1D_graph_coinmarketcap.csv"
        input_csv_path = os.path.join(current_dir, input_csv_name)
        output_csv_name = input_csv_name.split(".csv")[0] +"_formatted.csv"
        output_csv_path = os.path.join(current_dir, output_csv_name)

        with open(output_csv_path, 'w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            with open(input_csv_path) as input_file:
                csv_reader = csv.reader(input_file, delimiter = ',')
                split_char = ";"
                header = retrieve_header(next(csv_reader))
                csv_writer.writerow(header)
                output_rows = []
                for row in csv_reader:
                    output_rows.append(row[0].split(split_char))
                csv_writer.writerows(output_rows)
    except:
        print("Exception in main")

def remove_non_ascii_chars(input_string: str)->str:
    try:
        non_ascii_chars = re.findall(r'[^\x00-\x7F]', input_string)
        if len(non_ascii_chars)>0:
            for char in non_ascii_chars:
                input_string = input_string.replace(char, "") 
    except:
        print("Error occurred when trying to remove non-ascii characters from string")

    return input_string

def retrieve_header(header_row:list)->list:    
    header = header_row[0].split(";")
    for header_cnt, item in enumerate(header):
        header[header_cnt] = remove_non_ascii_chars(item)
    return header

if __name__ == "__main__":
    main()