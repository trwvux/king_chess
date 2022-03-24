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
            ["--", "--", "--", "--", "--", "--", "--", "--"],
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

    def get_chess_notation(self):  # toạ độ theo kí hiệu nước đi ( D1 : D3 ) // Tốt D1 lên Tốt D3
        return self.get_rank_files(self.startRow, self.startCol) + self.get_rank_files(self.endRow, self.endCol)

    def get_rank_files(self, row, col):  # toạ độ theo kí hiệu ( A1)
        return self.columns_to_file[col] + self.rows_to_ranks[row]
