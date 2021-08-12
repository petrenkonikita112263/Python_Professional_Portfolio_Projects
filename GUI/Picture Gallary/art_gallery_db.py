import sqlite3


class ArtGalleryDatabase:
    """ The base class representing a connection to database using sqlite3. """

    def __init__(self, file):
        """
        Initialize the ArtGalleryDatabase class with a database file, with
        connection value as None.
        """
        self.file = file
        self._connection = None

    @property
    def connection(self):
        """
        Method that returns the value of a private attribute without using any getter methods.
        :return: connection to the database
        """
        return self._connection

    @connection.setter
    def connection(self, input_connection):
        """
        Method that changes the value of a private attribute.
        :param input_connection: custom user's connection to database
        :return:
        """
        self._connection = input_connection

    def __enter__(self):
        """
        Method allows call this class or its object in with statement.
        After connection to database it returns the cursor
        :return: cursor that allow to execute the sql script
        """
        self._connection = sqlite3.connect(self.file)
        self._connection.row_factory = sqlite3.Row
        return self._connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Method which calls in the end of the with statement to close the connection
        to the database. Decides whether to commit or roll back.
        In any case sets the value of connection field to None.
        :param exc_type: type of exception
        :param exc_val: value of exception
        :param exc_tb: stack traceback message
        :return:
        """
        if exc_val:
            self._connection.rollback()
        else:
            self._connection.commit()
        # close connection
        try:
            self._connection.close()
        except AttributeError:
            # TODO 1: add logging writing if any errors are happened
            pass
        finally:
            self._connection = None

    def __str__(self) -> str:
        """
        Method that represents class as a string.
        :return: formatted string
        """
        return f"ArtGalleryDatabase: database {self.file} connect to {self.connection}"
