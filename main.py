from typing import final



@final
class TicTacToe:
    """A class that models TicTacToe, and beats you every time"""
    def __init__(self, human_starts: bool) -> None:
        self._board = ["_"] * 9
        self._turn = "human" if human_starts else "robot"
        self._human_goes_first = True if human_starts else False
        self._pieces = {"human": "X" if human_starts else "O", "robot": "O" if human_starts else "X"}
        self._turn_num = 0
        self._winner = None
    def human_move(self, human_move: int):
        self._board[human_move] = self._pieces["human"]
        self._turn_num += 1
    def robot_move(self):
        #we're gonna just implement the wikihow strategy to start

    def ascii_display(self):
        print("-"*9)
        for i in range(0,9):
            print(f" {self._board[i]} ", end="")
            if (i+1) % 3 == 0:
                print("\n")
        print("-"*9)
    def did_letter_win(self, letter: str, eval_board=None) -> bool:
        if eval_board is None:
            eval_board = self._board
        for i in range(0,3):
            if "".join(eval_board[0+i:i+2]) == letter*3:
                return True
        for i in range(0,3):
            if eval_board[i] + eval_board[i+3] + eval_board[i+6] == letter*3:
                return True
        return False

if __name__ == "__main__":
    ttt = TicTacToe(human_starts=False)

    while True:
        ttt.robot_move()
        ttt.ascii_display()
        ttt.human_move(int(input("choose (1-9) >")) - 1)
        ttt.ascii_display()
