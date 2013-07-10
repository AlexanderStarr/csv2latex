# ExcelToLaTeX Table Converter
# Takes .csv files as input, and converts them to
# a rudimentary table in LaTeX syntax

import csv

def create_header(first_line, output_file, just):
    column = " | " + just
    output_file.write(r"\begin{tabular}{" + len(first_line) * column + r" | } " + "\n")
    output_file.write(r"\hline" + "\n")
    add_data(first_line, output_file)

def add_data(current_line, output_file):
    new_line = ""
    for element in current_line:
        new_line = new_line + element + " & "
    new_line = new_line[0:len(new_line) - 2] + r"\\" +"\n"
    output_file.write(new_line)
    output_file.write(r"\hline" + "\n")

file_name = str(raw_input("Enter the file name: "))
just = str(raw_input("What justification (r, l, or c)?: "))
with open(file_name, "rU") as csvfile:
    input_file = csv.reader(csvfile)
    with open("output.txt", "w") as output_file:
        create_header(input_file.next(), output_file, just)
        for line in input_file:
            add_data(line, output_file)
