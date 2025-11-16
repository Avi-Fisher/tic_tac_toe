from Creat_board import Creat_board

class Board:

    def __init__(self):

        self.board = Creat_board.creat()



    def update_coisc(self,player,location):

        self.board[location[0]][location[1]] = player



    def check_if_win(self,turn):

        count = 1

        if self.board[]




