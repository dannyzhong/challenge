from little_date_calculator.error import CSVFileLoadError
import csv


class CSVLoader:
    def __init__(self):
        None

    @classmethod
    def load(cls, input_file):
        try:
            with open(input_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                return [row for row in reader]
        except:
            raise CSVFileLoadError("Load input csv file error")


class SourceLoader:
    def __init__(self, file_format: str):
        self._loader = None
        self.update_file_format(file_format)

    def update_file_format(self, file_format: str):
        if file_format == "csv":
            self._loader = CSVLoader()

    def load(self, input_file):
        try:
            return self._loader.load(input_file)
        except:
            raise