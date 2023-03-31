import unittest
from main import TicTacToe

class TicTacToeTestCase(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_draw_board(self):
        # Проверка отрисовки игрового поля
        expected_board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.assertListEqual(self.game.board, expected_board)

    def test_check_win(self):
        # Проверка выигрышных комбинаций
        self.game.board = [
            ['X', 'O', 'O'],
            ['X', 'X', 'O'],
            ['X', '', '']
        ]
        self.assertTrue(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))

    def test_play_game(self):
        # Проверка игрового процесса
        self.game.current_player = 'X'
        self.game.board = [
            ['X', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.game.run()
        expected_board = [
            ['X', '', ''],
            ['O', '', ''],
            ['', '', '']
        ]
        self.assertListEqual(self.game.board, expected_board)

if __name__ == '__main__':
    unittest.main()