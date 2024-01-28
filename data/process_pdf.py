import tabula
import argparse

parser = argparse.ArgumentParser(description='convert pdf to csv')
parser.add_argument("-i", help = "input file name", type = str, default = "pdf_name")
parser.add_argument("-o", help = "output file name", type = str, default = "csv_file_name")
args = parser.parse_args()



if __name__ == '__main__':
    args = parser.parse_args()
    input_file = args.i
    output_file = args.o
    df = tabula.read_pdf(input_file, pages='all')[0]
    tabula.convert_into(input_file, output_file, output_format="csv", pages='all')

