class GameState():
    def __init__(self):
        # bàn cờ 8x8
        # b đại diện cho quân trắng, w đai diện cho quân đen
        # "--" đại diện cho khoảng trắng
        # R là Xe, N là Mã, B là Tượng, Q là Hậu, K là Vua, P là Tốt
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "bP", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        # lượt đi của quân trắng
        self.whiteToMove = True
        # nhật ký di chuyển
        self.moveLog = []

    def make_move(self, move):
        self.board[move.startRow][move.startCol] = "--"  # gán ô click đầu tiên trống (vị trí quân cờ click đầu tiên)
        self.board[move.endRow][move.endCol] = move.piece_move  # gắn vị trí mới cho quân cờ
        self.moveLog.append(move)  # thêm vào log để undo it later
        self.whiteToMove = not self.whiteToMove  # hết lượt quân trắng, lượt quân đen đi

    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][
                move.startCol] = move.piece_move
            self.board[move.endRow][move.endCol] = move.piece_captured
            self.whiteToMove = not self.whiteToMove  # đổi lượt

    # ALl moves considering checks
    def get_valid_moves(self):
        return self.get_all_possible_moves()

    # ALl moves without considering checks
    def get_all_possible_moves(self):
        moves = []
        for row in range(8):
            for col in range(8):
                turn = self.board[row][col][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    if piece == "P":
                        self.get_pawn_moves(row, col, moves)
                    elif piece == "R":
                        self.get_rook_move(row, col, moves)
                    elif piece == "N":
                        self.get_knight_move(row, col, moves)
                    elif piece == "B":
                        self.get_bishop_moves(row, col, moves)
                    elif piece == "Q":
                        self.get_queen_moves(row, col, moves)
                    elif piece == "K":
                        self.get_king_moves(row, col, moves)
        return moves

    def get_pawn_moves(self, row, col, move):  # quy tắc đi của quân tốt
        if self.whiteToMove:
            if self.board[row - 1][col] == "--":
                move.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == "--":
                    move.append(Move((row, col), (row - 2, col), self.board))
            if col - 1 >= 0: # ăn quân bên trái
                if self.board[row - 1][col - 1][0] == 'b':
                    move.append(Move((row, col), (row - 1, col - 1), self.board))
            if col + 1 < 7: #ăn quân bên phải
                if self.board[row - 1][col + 1][0] == 'b':
                    move.append(Move((row, col), (row - 1, col + 1), self.board))
        else:  # black move
            pass

    def get_rook_move(self, row, col, move):  # quy tắc đi của quân xe
        pass

    def get_bishop_moves(self, row, col, move):  # quy tắc đi của quân mã
        pass

    def get_knight_move(self, row, col, move):  # quy tắc đi của quân tượng
        pass

    def get_queen_moves(self, row, col, move):  # quy tắc đi của quân hậu
        pass

    def get_king_moves(self, row, col, move):  # quy tắc đi của quân vua
        pass


class Move():
    # maps key to value
    # key : value
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_columns = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    columns_to_file = {v: k for k, v in files_to_columns.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]  # toạ độ cột của lần click đầu tiên
        self.startCol = startSq[1]  # toạ độ hàng của lần click đầu tiên
        self.endRow = endSq[0]  # toạ độ cột của lần click thứ hai
        self.endCol = endSq[1]  # toạ độ hàng của lần click thứ hai
        self.piece_move = board[self.startRow][self.startCol]  # vị trí quân cờ đc chọn để di chuyển
        self.piece_captured = board[self.endRow][self.endCol]  # ảnh chụp tạo độ sau khi di chuyển( để undo nước đi)
        self.move_id = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    # Overriding the equal method
    def __eq__(self, other):
        if (isinstance(other, Move)):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):  # toạ độ theo kí hiệu nước đi ( D1 : D3 ) // Tốt D1 lên Tốt D3
        return self.get_rank_files(self.startRow, self.startCol) + self.get_rank_files(self.endRow, self.endCol)

    def get_rank_files(self, row, col):  # toạ độ theo kí hiệu ( A1)
        return self.columns_to_file[col] + self.rows_to_ranks[row]
