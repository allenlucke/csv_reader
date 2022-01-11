# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


with open('bnkAcct.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if not row[4]:
                print(f' Income  ------ Date: \t{row[1]} ; Description: {row[2]} ; Amount Credit: {row[5]}')
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            else:
                print(f' Expense ------ Date: \t{row[1]} ; Description: {row[2]} ; Amount Debit: {row[4]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
