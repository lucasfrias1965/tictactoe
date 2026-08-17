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
        #okay, we are gonna win based off of the position but
        # instead of (sanely) using the finite solution, we are going to make a BST
        # of all potential positions.

    def ascii_display(self):
        print("-"*9)
        for i in range(0,9):
            print(f" {self._board[i]} ", end="")
            if (i+1) % 3 == 0:
                print("\n")
        print("-"*9)

if __name__ == "__main__":
    ttt = TicTacToe(human_starts=True)
    ttt.ascii_display()
    ttt.human_move(int(input("choose (1-9) >")) - 1)
