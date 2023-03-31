import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размер окна
WINDOW_SIZE = (500, 500)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размер клетки
CELL_SIZE = 100

# Класс для игры
class TicTacToe:
    def __init__(self):
        # Создание окна
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Крестики-нолики")

        # Создание игрового поля
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

        # Текущий игрок
        self.current_player = 'X'

    # Функция для отрисовки игрового поля
    def draw_board(self):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(self.screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
                font = pygame.font.SysFont('comicsansms', 50)
                text = font.render(self.board[row][col], True, WHITE)
                self.screen.blit(text, (col * CELL_SIZE + 25, row * CELL_SIZE + 25))

    # Функция для проверки выигрышных комбинаций
    def check_win(self, player):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    # Основной цикл игры
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    row = mouse_pos[1] // CELL_SIZE
                    col = mouse_pos[0] // CELL_SIZE
                    if self.board[row][col] == '':
                        self.board[row][col] = self.current_player
                        if self.check_win(self.current_player):
                            print(self.current_player + ' wins!')
                            pygame.quit()
                            sys.exit()
                        if self.current_player == 'X':
                            self.current_player = 'O'
                        else:
                            self.current_player = 'X'
            self.screen.fill(BLACK)
            self.draw_board()
            pygame.display.update()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()