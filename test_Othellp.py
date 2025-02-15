import unittest
from Othello import Player, Othello


class TestOthello(unittest.TestCase):
    def test_player(self):
        """Tests the player class initialization and get functions"""
        new_player = Player("John", 'black')
        self.assertEqual(new_player.get_name(), "John")
        self.assertEqual(new_player.get_color(), 'black')

    def test_init(self):
        game = Othello()
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'O', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertIsNone(game._player1)
        self.assertIsNone(game._player2)

    def test_create_player(self):
        """Test player creation"""

        # Test two valid players initialized
        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "black")

        self.assertEqual(game._player1.get_name(), "Helen")
        self.assertEqual(game._player1.get_color(), 'white')
        self.assertEqual(game._player2.get_name(), "Leo")
        self.assertEqual(game._player2.get_color(), 'black')

        # Test that trying to add a third player will not work
        game.create_player("John", "black")

        self.assertEqual(game._player1.get_name(), "Helen")
        self.assertEqual(game._player1.get_color(), 'white')
        self.assertEqual(game._player2.get_name(), "Leo")
        self.assertEqual(game._player2.get_color(), 'black')

        # Test that trying to create two players with the same color will not work
        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "white")

        self.assertEqual(game._player1.get_name(), "Helen")
        self.assertEqual(game._player1.get_color(), 'white')
        self.assertIsNone(game._player2)

        # Test that trying to create a player with an invalid color will not work
        game.create_player("Leo", "brown")
        self.assertEqual(game._player1.get_name(), "Helen")
        self.assertEqual(game._player1.get_color(), 'white')
        self.assertIsNone(game._player2)

    def test_return_winner(self):
        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "black")

        game._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        results = game.return_winner()
        self.assertEqual(results, "Winner is black player: Leo")

        game._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        results = game.return_winner()
        self.assertEqual(results, "Winner is white player: Helen")

        game._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        results = game.return_winner()
        self.assertEqual(results, "It's a tie")

    def test_return_available_positions(self):
        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "black")

        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "black")

        # Make a series of plays, checking the available positions after each move
        expected_white_moves = [(3, 5), (4, 6), (5, 3), (6, 4)]
        expected_black_moves = [(3, 4), (4, 3), (5, 6), (6, 5)]
        self.assertListEqual(game.return_available_positions('white'), expected_white_moves)
        self.assertListEqual(game.return_available_positions('black'), expected_black_moves)

        game.play_game("black", (5, 6))
        expected_white_moves = [(4, 6), (6, 4), (6, 6)]
        expected_black_moves = [(3, 3), (3, 4), (4, 3)]
        self.assertListEqual(game.return_available_positions('white'), expected_white_moves)
        self.assertListEqual(game.return_available_positions('black'), expected_black_moves)

        game.play_game("white", (6, 6))
        expected_white_moves = [(3, 5), (4, 6), (5, 3), (5, 7), (6, 4)]
        expected_black_moves = [(3, 4), (4, 3), (6, 5), (7, 6)]
        self.assertListEqual(game.return_available_positions('white'), expected_white_moves)
        self.assertListEqual(game.return_available_positions('black'), expected_black_moves)

        game.play_game("black", (6, 5))
        expected_white_moves = [(4, 6), (6, 4)]
        expected_black_moves = [(3, 3), (3, 4), (4, 3), (6, 7), (7, 6), (7, 7)]
        self.assertListEqual(game.return_available_positions('white'), expected_white_moves)
        self.assertListEqual(game.return_available_positions('black'), expected_black_moves)

    def test_make_move(self):
        """Tests that making moves works correctly. This also tests the capture method by extension"""
        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "black")

        board = game.make_move("black", (5, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("white", (6, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'O', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("black", (6, 5))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', 'X', 'O', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("white", (6, 4))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("black", (7, 3))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'O', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("white", (7, 4))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'O', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("black", (7, 5))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("white", (8, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'O', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("black", (7, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

        board = game.make_move("white", (6, 7))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(board, expected_board)

    def test_play_game(self):
        game = Othello()
        game.create_player("Helen", "white")
        game.create_player("Leo", "black")

        # Test a series of valid moves
        game.play_game("black", (5, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("white", (6, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'O', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("black", (6, 5))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', 'X', 'O', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("white", (6, 4))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("black", (7, 3))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'X', 'O', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("white", (7, 4))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'O', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("black", (7, 5))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("white", (8, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'O', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'O', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("black", (7, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        game.play_game("white", (6, 7))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)

        # Try to make a few invalid moves
        return_statement = game.play_game("black", (1, 1))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("white", (1, 1))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("black", (3, 5))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("white", (6, 3))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("white", (5, 4))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("white", (5, 5))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("white", (6, 8))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        return_statement = game.play_game("white", (5, 6))
        expected_board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', 'O', 'O', 'O', 'O', '.', '*'],
                          ['*', '.', '.', 'X', 'X', 'X', 'X', '.', '.', '*'],
                          ['*', '.', '.', '.', '.', '.', 'O', '.', '.', '*'],
                          ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self.assertListEqual(game._board, expected_board)
        self.assertEqual(return_statement, "Invalid move")

        # Set the board to be one move away from a win condition then make the final move
        # This will test the end of game
        game._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '*'],
                       ['*', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        game.play_game('white', (8, 8))


if __name__ == '__main__':
    unittest.main()
