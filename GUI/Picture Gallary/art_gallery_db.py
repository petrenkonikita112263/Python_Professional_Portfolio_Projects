import sqlite3


class ArtGalleryDatabase:
    """Class that implements the sqlite3 functionality"""

    def __init__(self, file):
        self.file = file
        self._connection = None

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, input_connection):
        self._connection = input_connection

    def __enter__(self):
        self._connection = sqlite3.connect(self.file)
        self._connection.row_factory = sqlite3.Row
        return self._connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Decide whether to commit or roll back"""
        if exc_val:
            self._connection.rollback()
        else:
            self._connection.commit()
        # close connection
        try:
            self._connection.close()
        except AttributeError:
            pass
        finally:
            self._connection = None

    def __str__(self) -> str:
        return f"ArtGalleryDatabase: database {self.file} connect to {self.connection}"
