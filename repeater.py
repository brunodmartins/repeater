import argparse
import csv
import subprocess


def read_all_lines(data_path):
    with open(data_path, 'r') as f:
            return f.readlines()

def read_csv_data(data_path):
    result = []
    with open(data_path, 'r', newline='') as csvfile:
        for row in csv.DictReader(csvfile):
            result.append(row)
    return result

def is_txt_data(data_path):
    return ".txt" in data_path

def is_csv_data(data_path):
    return ".csv" in data_path

def execute_command(command, data_path, verbose=False):
    if is_txt_data(data_path):
        data = read_all_lines(data_path)
        for line in data:
            subprocess.run([command, line.strip()])
    elif is_csv_data(data_path):
        data = read_csv_data(data_path)
        for row in data:
            final_command = command
            for key in row.keys():
                pattern = "{" + key + "}"
                final_command = final_command.replace(pattern, row[key])
            result = subprocess.run([final_command], shell=True, stdout=subprocess.PIPE)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Required arguments")
    parser.add_argument('--command', type=str, help='The command to be executed')
    parser.add_argument('--data', type=str, help='The data to be executed with the command')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

    args = parser.parse_args()
    execute_command(args.command, args.data, args.verbose)

