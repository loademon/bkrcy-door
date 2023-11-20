class Error(Exception):
    """Base class for exceptions"""

    def __init__(self, msg: str) -> None:
        self.message = msg
