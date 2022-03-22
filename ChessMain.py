import pygame
import ChessEngine

pygame.init()
clock = pygame.time.Clock()
width = 512
height = 512
dimension = 8
max_FPS = 15
sq_size = height / dimension
images = {}


# load images
def load_images():
    pieces = ['bB', 'bK', 'bN', 'bP', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wP', 'wQ', 'wR']
    # call images['bB']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (sq_size, sq_size))


# draw game state
def draw_game_state(screen,board):
    draw_board(screen)
    draw_pieces(screen, board)


# draw board
def draw_board(screen):
    colors = [(pygame.Color("white")), (pygame.Color("gray"))]
    for row in range(dimension):
        for column in range(dimension):
            color = colors[(row + column) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(column * sq_size, row * sq_size, sq_size, sq_size))


def draw_pieces(screen, board):
    for row in range(dimension):
        for column in range(dimension):
            piece = board[row][column]
            if piece != "--":  # nếu hình vuông không trống
                screen.blit(images[piece], pygame.Rect(column * sq_size, row * sq_size, sq_size, sq_size))


if __name__ == "__main__":
    # tạo cửa sổ
    screen = pygame.display.set_mode((width, height))
    # load ảnh
    load_images()
    pygame.display.set_caption("Vũ đẹp trai siêu cấp vũ trụ")
    pygame.display.set_icon(images['bN'])
    screen.fill(pygame.Color("white"))
    gs = ChessEngine.GameState()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_game_state(screen, gs.board)
        clock.tick(max_FPS)  # fps
        pygame.display.flip()
