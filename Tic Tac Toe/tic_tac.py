class TicTacToeGame:

    def __init__(self, board) -> None:
        """Class constructor"""
        self.board = board

    def display_board(self) -> None:
        """Function that sets up the board as the list"""
        print(f"""
        -------------------------
        |\t{self.board[1]}\t|\t{self.board[2]}\t|\t{self.board[3]}\t|
        -------------------------
        |\t{self.board[4]}\t|\t{self.board[5]}\t|\t{self.board[6]}\t|
        -------------------------
        |\t{self.board[7]}\t|\t{self.board[8]}\t|\t{self.board[9]}\t|
        -------------------------
        """)

    def place_marker(self, marker: str, position: int) -> None:
        """Function that places player's marker on board with specific position"""
        self.board[position] = marker

    def have_winning_position(self, mark) -> bool:
        """Method that checks every possible way to win the game"""
        return ((self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) or  # across the top
                (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) or  # across the middle
                (self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) or  # across the bottom
                (self.board[1] == mark and self.board[4] == mark and self.board[7] == mark) or  # left top to down
                (self.board[2] == mark and self.board[5] == mark and self.board[8] == mark) or  # middle top to down
                (self.board[3] == mark and self.board[6] == mark and self.board[9] == mark) or  # right top to down
                (self.board[1] == mark and self.board[5] == mark and self.board[9] == mark) or  # diagonal-1
                (self.board[7] == mark and self.board[5] == mark and self.board[3] == mark))  # diagonal-2

    def check_the_cell(self, position: int) -> bool:
        """Check the specific cell on the board for emptiness"""
        return self.board[position] == " "

    def check_the_board(self):
        """Check if the board is full covered"""
        for i in range(1, 10):
            if self.check_the_cell(i):
                return False
        return True
