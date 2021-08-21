from little_date_calculator.error import CSVFileOutputError
import csv


class CSVWriter:
    def __init__(self):
        None

    @classmethod
    def output(cls, output_file, result: list):
        try:
            with open(output_file, 'w') as f:
                writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(["count"])
                for item in result:
                    writer.writerow([item])
        except:
            raise CSVFileOutputError("Write result to csv file error")


class OutputWriter:
    def __init__(self, file_format: str):
        self._writer = None
        self.update_file_format(file_format)

    def update_file_format(self, file_format: str):
        if file_format == "csv":
            self._writer = CSVWriter()

    def write(self, output_file: str, result: list):
        try:
            return self._writer.output(output_file, result)
        except:
            raise