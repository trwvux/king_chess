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
            ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"],
        ]
        # lượt đi của quân trắng
        self.whiteToMove = True
        # nhật ký di chuyển
        self.moveBlog = []
