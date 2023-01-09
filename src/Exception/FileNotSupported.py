

class FileNotSupported(Exception):

    def __init__(self) -> None:
        message = 'This file type is not supported'
        super().__init__(message)
