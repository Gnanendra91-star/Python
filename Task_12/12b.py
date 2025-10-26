import pygame

# Initialize pygame
pygame.init()

# Set screen size and title
screen_size = (640, 640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Chess Board')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
brown = (153, 76, 0)

# Define function to draw the board
def draw_board():
    for row in range(8):
        for col in range(8):
            square_color = white if (row + col) % 2 == 0 else brown
            square_rect = pygame.Rect(col * 80, row * 80, 80, 80)
            pygame.draw.rect(screen, square_color, square_rect)

# Define function to draw the pieces
def draw_pieces(board):
    SQUARE_SIZE = 80  # or whatever your square size is

    piece_images = {
    
    'p': pygame.transform.scale(pygame.image.load('E:/SUMMER 25_26/PYTHON/lab/New folder/pawn.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'r': pygame.transform.scale(pygame.image.load('E:/SUMMER 25_26/PYTHON/lab/New folder/rook.jpg'), (SQUARE_SIZE, SQUARE_SIZE)),
    'n': pygame.transform.scale(pygame.image.load('E:/SUMMER 25_26/PYTHON/lab/New folder/knight.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'b': pygame.transform.scale(pygame.image.load('E:/SUMMER 25_26/PYTHON/lab/New folder/bishop.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'q': pygame.transform.scale(pygame.image.load('E:/SUMMER 25_26/PYTHON/lab/New folder/queen.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'k': pygame.transform.scale(pygame.image.load('E:/SUMMER 25_26/PYTHON/lab/New folder/king.png'), (SQUARE_SIZE, SQUARE_SIZE))
}

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '.':
                piece_image = piece_images[piece]
                piece_rect = pygame.Rect(col * 80, row * 80, 80, 80)
                screen.blit(piece_image, piece_rect)



# Define initial state of the board
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

# Draw board and pieces
draw_board()
draw_pieces(board)

# Start game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

