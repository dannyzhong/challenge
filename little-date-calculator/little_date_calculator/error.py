class ValidationError(Exception):
    """ An input parameter is invalid. """

class FormatError(Exception):
    """ An input date format not supported. """

class CSVFileLoadError(Exception):
    """ csv file loading error. """

class CSVFileOutputError(Exception):
    """ csv file output error"""