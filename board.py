

class Board:
    def __init__(self, board_data) -> None:
        """Creates a board, requires a list called board_data which contains a 3x3 2D array with
        capatilized single character strings such as "X".
        Instance will contain three pieces of information:
            data -> the same 3x3 2D list passed
            won -> a boolean that determines if there is a winner
            winner -> a string, either "human" if O, "computer" if X, or "none" if won is false.
        """
        self.data = board_data
        self.won = False
        self.winner = "none"
        #the board's winner is pre computed
        #first we iterate through every single column by fixing the x,
        #then we iterate through every single row by fixing the y
    def check_for_win(self) -> None:
        for x in range(3):
            if self.data[0][x] == self.data[1][x] == self.data[2][x]:
                self.won = True
                if self.data[0][x] == "X":
                    self.winner = "computer"
                else:
                    self.winner = "human"

        for y in range(3):
            if self.data[y][0] == self.data[y][1] == self.data[y][2]:
                self.won = True
                if self.data[y][0] == "X":
                    self.winner = "computer"
                else:
                    self.winner = "human"

        #diagonal check now:
        #from the farthest to the closest and reverse again
        if self.data[0][0] == self.data[1][1] == self.data[2][2]:
            self.won = True
            if self.data[0][0] == "X":
                self.winner = "computer"
            else:
                self.winner = "human"

        if self.data[2][0] == self.data[1][1] == self.data[0][2]:
            self.won = True
            if self.data[0][0] == "X":
                self.winner = "computer"
            else:
                self.winner = "human"

def get_best_path(prime_board):
    best_solution = None
    valid_indeces = []
    for i in range(prime_board):
        if board[i] == "_":
            valid_indeces.append(i)
    #we now have a valid list of all free indices.
    # we're now going to evaluate what would happen if we put an X in them
    for i in valid_indeces:
        potential_board = prime_board[i] = "_"
        potential_board.check_for_win()
        if potential_board == "X":
            pass
        res = get_best_path(potential_boaard)
