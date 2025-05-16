import sys
import csv
from argparse import ArgumentParser, FileType

parser = ArgumentParser()
parser.add_argument('--in-delimiter', type=str, default="|")
parser.add_argument('--in-quote', type=str, default='"')
parser.add_argument('input', type=FileType("rt"))
parser.add_argument('output', type=FileType("wt"))

args = parser.parse_args()

reader = csv.reader(args.input, delimiter=args.in_delimiter, quotechar=args.in_quote)
writer = csv.writer(args.output)

for line in reader:
    writer.writerow(line)