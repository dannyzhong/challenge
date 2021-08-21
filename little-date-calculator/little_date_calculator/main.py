import argparse
import sys
from argparse import RawTextHelpFormatter
from little_date_calculator.date_input_parser import DateInputParser
from little_date_calculator.date_calculator import DateCalculator
from little_date_calculator.source_loader import SourceLoader
from little_date_calculator.output_writer import OutputWriter

OUTPUT_TEMPLATE = "The days between %s and %s is %s days"


def arguments_parser():
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description="My little date calculator")
    parser.add_argument("--date-format", help="the input date format", default="dd/mm/yyyy")
    parser.add_argument("-s", "--start-date", help="start date for the date calculation", type=str, required='--input-file' not in sys.argv)
    parser.add_argument("-e", "--end-date", help="end date for the date calculation", type=str, required='--input-file' not in sys.argv)
    parser.add_argument("--input-file", help="input source file")
    parser.add_argument("--input-file-format", choices=["csv"] ,help="input file format", default="csv")
    parser.add_argument("--output-file", help="output file", required='--input-file' in sys.argv )
    parser.add_argument("--output-file-format", choices=["csv"], help="output file format", default="csv")
    return parser


def main():
    args = arguments_parser().parse_args()
    parser = DateInputParser(date_format=args.date_format)
    calculator = DateCalculator()
    if args.input_file:
        loader = SourceLoader(args.input_file_format)
        result = []
        for date_range in loader.load(args.input_file):
            start_date_parsed = parser.parse(date_range[0].strip())
            end_date_parsed = parser.parse(date_range[1].strip())
            result.append(str(calculator.diff(start_date=start_date_parsed, end_date=end_date_parsed)))
        writer = OutputWriter(args.input_file_format)
        writer.write(args.output_file, result)
    else:
        start_date_parsed = parser.parse(args.start_date)
        end_date_parsed = parser.parse(args.end_date)
        print(OUTPUT_TEMPLATE%(args.start_date,
                               args.end_date,
                               str(calculator.diff(start_date=start_date_parsed, end_date=end_date_parsed))))


if __name__ == '__main__':
    sys.exit(main())