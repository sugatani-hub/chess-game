import pygame
import chess_engine

MAX_FPS = 24
BOARD_WIDTH = BOARD_HEIGHT = 480
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
IMAGES = {}
COLORS = ["#FFF5E1","#855E42"]

def load_images():
    pieces = ["bR","bN","bB","bQ","bK","bP","wP","wK","wQ","wB","wN","wR"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("../images/" + piece + ".png"),(SQUARE_SIZE,SQUARE_SIZE)) #pygame.transform.scaleによって、画像がSQUARE_SIZEに収まるように調整

def draw_game_status(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = COLORS[((row+col)%2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE ,SQUARE_SIZE))

def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "  ":
                screen.blit(IMAGES[piece], pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE ,SQUARE_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_WIDTH,BOARD_HEIGHT))
    clock = pygame.time.Clock()
    load_images()
    gs = chess_engine.Game_Status()
    player_click = []
    flg_running = True
    print("Game Start\nturn: White")
    while flg_running:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE
                player_click.append([row, col])
                print(player_click)
                if len(player_click) == 2:
                    if gs.check_move(player_click) and gs.check_move_piece(player_click):
                        gs.make_move(player_click)
                        if gs.checkmate():
                            flg_running = False
                            print("Checkmate")
                        turn = "White" if gs.player else "Black"
                        print(f"Success!\n{turn} turn:")
                    else:
                        print("Invalid move")
                    player_click = []
        draw_game_status(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()
if __name__ == "__main__":
    main()