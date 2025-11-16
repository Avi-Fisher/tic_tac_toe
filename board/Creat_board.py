
class Creat_board:

    @staticmethod
    def creat():
        square = "clear"

        board = []
        for i in range(3):
            coulm = []

            for j in range(3):
                coulm.append(square)

            board.append(coulm)
        return board