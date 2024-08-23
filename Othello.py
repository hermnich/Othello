# Author: Nick Herman
# GitHub username: hermnich
# Date: 2023/06/09
# Description: The game Othello. Contains a class Othello to handle the game play, and a Player class used by Othello
# to handle player data

class Player:
    """Defines a player, with a name and color. Used by the Othello class"""

    def __init__(self, name, color):
        """Constructs the player with the given name and color"""
        self._name = name
        self._color = color

    def get_name(self):
        """Returns the player's name"""
        return self._name

    def get_color(self):
        """Returns the player's color"""
        return self._color


class Othello:
    """Represents a game of Othello. Manages the game board, players, and any moves that are made.
    Uses the Player class for storing player information."""

    def __init__(self):
        """Takes no parameters. Initializes the game of Othello with all of the required data members."""
        self._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', 'X', 'O', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self._player1 = None
        self._player2 = None

    def print_board(self):
        """Takes no parameters. Prints out the current layout of the game board.
        Key is as follows:
        Edge:           '*'
        Black Piece:    'X'
        White Piece:    'O'
        Empty Space:    '.'"""

        for row in self._board:
            row_string = ''
            for column in row:
                row_string += column + ' '
            print(row_string)

    def create_player(self, player_name, color):
        """Parameters:
            player_name - string containing the name of the player
            color - represents the color of the game tiles the player will use. Valid colors are 'black' or 'white'
        Creates a player object with the given name and color and adds it to the game's player list.
        Only two players can be created and they must have different colors."""

        # Check if there is a Player in player2.
        # If there is, then both players have already been created and a new one cannot be added.
        if self._player2 is not None:
            print("Cannot create player. Two players have already been created.")
            return

        # Validate that the color entered is either 'black' or 'white'
        if color != 'black' and color != 'white':
            print("Cannot create player. Please verify that the color entered is either 'black' or 'white'.")
            return

        # If there is already a player in player 1, validate the color for player1 is different than the color entered,
        # then create the new player in player2
        if self._player1 is not None:
            if self._player1.get_color() == color:
                print("Cannot create player. A player with that color already exists.")
                return
            self._player2 = Player(player_name, color)

        # If there is no player1, create the new player as player1
        else:
            self._player1 = Player(player_name, color)

    def return_winner(self):
        """Takes no parameters. Returns the player with the highest number of tiles on the board.
        In the event that both players have the same number of tiles, returns 'it is a tie!'"""

        # Check each position on the board, totaling up black and white tiles
        black_tiles = 0
        white_tiles = 0
        for row in self._board:
            for column in row:
                if column == 'X':
                    black_tiles += 1
                if column == 'O':
                    white_tiles += 1

        # Once the whole board has been totaled, compare the values
        # If the values are the same, print out the message for a tie
        if black_tiles == white_tiles:
            return "It's a tie"

        # If the black value is higher, check the color of each of the players and get the name of the black player.
        # Print out the message that black has one containing the player name
        if black_tiles > white_tiles:
            if self._player1.get_color() == 'black':
                player_name = self._player1.get_name()
            else:
                player_name = self._player2.get_name()
            return_str = "Winner is black player: " + player_name
            return return_str

        # Else white is higher. Repeat the process above but for the white player.
        else:
            if self._player1.get_color() == 'white':
                player_name = self._player1.get_name()
            else:
                player_name = self._player2.get_name()
            return_str = "Winner is white player: " + player_name
            return return_str

    def return_available_positions(self, color):
        """Parameters:
            color - the color of game tile to check for available positions. Valid colors are 'black' or 'white'
        Returns a list of all possible positions that the given color can currently make a move.
        Positions are represented as a tuple in (row, column) form"""

        available_positions = []
        # Check each position on the board for a blank space.
        for row in range(10):
            for column in range(10):
                # If a blank space is found, then it needs to be checked for a valid play.
                # To check for a valid capture, call the check_capture method passing a color and position.
                # If check_capture returns True, there is at least one valid capture path leading from the current blank space.
                # add this to the list of available positions
                if self._board[row][column] == '.' and self.check_capture(color, (row, column)):
                    available_positions.append((row, column))

        # Once all of the positions on the board have been checked, return the list of available positions.
        return available_positions

    def make_move(self, color, piece_position):
        """Parameters:
           color - the color of tile making the move. Valid colors are 'black' or 'white'
           piece_position - The position on the board that the piece is being placed. Must be a tuple in (row, column) form
        Places a tile of the specified color in the specified position on the game board,
        captures any relevant pieces, and prints the updated board."""

        # Change the board data at the specified location so that it contains a piece for the specified color
        if color == 'black':
            self._board[piece_position[0]][piece_position[1]] = 'X'
        else:
            self._board[piece_position[0]][piece_position[1]] = 'O'

        # call the capture method
        self.capture(color, piece_position)

        # return the current board
        return self._board

    def play_game(self, player_color, piece_position):
        """Parameters:
            player_color - the color of tile that is being played. Valid colors are 'black' or 'white'
            piece_position - The position on the board that the piece is being placed. Must be a tuple in (row, column) form
        Attempts to make a move for the player with the given color in the given position.
        If the move being attempted is not a valid move, the move will not be made and a list of
        available moves will be printed instead. If the move results in the end of the game,
        the final scores and the winner will be printed."""

        # validate the move by calling return_available_positions for the player making the move and checking if the
        # position is in the list returned
        valid_positions = self.return_available_positions(player_color)
        if piece_position not in valid_positions:
            # If it is not, print out the list of valid moves received previously and return 'invalid move'.
            print(f"Here are the valid moves: {valid_positions}")
            return "Invalid move"

        # If it is, the move is a valid move. call make_move
        self.make_move(player_color, piece_position)

        # To check if the game is over, call return_available_positions for both players.
        # If both lists return empty, then the game is over. Call return_winner then print out the final results
        available_white_moves = self.return_available_positions('white')
        available_black_moves = self.return_available_positions('black')

        if available_white_moves == [] and available_black_moves == []:
            # Count the tiles of each color on the board
            black_tiles = 0
            white_tiles = 0
            for row in self._board:
                for column in row:
                    if column == 'X':
                        black_tiles += 1
                    if column == 'O':
                        white_tiles += 1

            winner = self.return_winner()
            print(f"Game has ended white piece: {white_tiles} black piece: {black_tiles}")
            print(winner)

    def check_capture(self, color, piece_position):
        """Parameters:
            color - the color of tile that is being played. Valid colors are 'black' or 'white'
            piece_position - The position on the board that the piece is being placed. Must be a tuple in (row, column) form
        Checks along the vertical, horizontal, and diagonal lines surrounding a specified board position for any
        valid capture lines.
        Returns True if a valid capture is found, or False if there are no captures from the specified position"""

        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in offsets:
            first_pos = (piece_position[0] + offset[0], piece_position[1] + offset[1])
            if color == 'black':
                if self._board[first_pos[0]][first_pos[1]] == 'O' and self.line_capture(color, piece_position, offset):
                    return True
            if color == 'white':
                if self._board[first_pos[0]][first_pos[1]] == 'X' and self.line_capture(color, piece_position, offset):
                    return True

    def capture(self, color, piece_position):
        """Parameters:
            color - the color of tile that is being played. Valid colors are 'black' or 'white'
            piece_position - The position on the board that the piece is being placed. Must be a tuple in (row, column) form
        Checks along the vertical, horizontal, and diagonal lines surrounding a newly played game piece and
        converts any of the opponent's pieces that have been successfully captured."""

        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for offset in offsets:
            self.line_capture(color, piece_position, offset, True)

    def line_capture(self, color, piece_position, direction_offset, capture=False):
        """Parameters:
            color - the color of tile that is being played. Valid colors are 'black' or 'white'
            piece_position - The position on the board that the piece is being placed. Must be a tuple in (row, column) form
            direction_offset - An offset corresponding to the direction on the board that capture is being checked in.
                Must be a tuple in (row, column) form.
                Valid offsets are shown below, along with how they will move the position.
                (-1, -1)    (-1, 0)     (-1, 1)
                (0, -1) piece_position  (0, 1)
                (1, -1)     (1, 0)      (1, 1)
            capture - Flag to determine if the method will also change the color of any captured tiles. Defaults to False
        Checks along a specific direction out from a board position to determine if there is a valid capture in that
        direction for the specified color. If the capture flag is left False, the board is not modified.
        Setting capture to True will additionally modify the color of any opponent tiles if a valid capture is found.
        Returns True if there is a capture, or False if there is not."""

        # Add an offset to the specified position depending on which direction is being checked.
        current_position = (piece_position[0] + direction_offset[0], piece_position[1] + direction_offset[1])

        # If a boundary character or blank space is found, then stop checking this line. It is not a valid capture line. Return False
        if self._board[current_position[0]][current_position[1]] == '*' or self._board[current_position[0]][current_position[1]] == '.':
            return False

        if color == 'black':
            # If a character of the specified color is found, this is a valid capture line. set the return value True
            if self._board[current_position[0]][current_position[1]] == 'X':
                return True

            # If there is a piece of the opposite color, continue to check along that line by calling itself again.
            if self._board[current_position[0]][current_position[1]] == 'O':
                return_val = self.line_capture(color, current_position, direction_offset, capture)

                # If the value to be returned is True, and the capture flag is True,
                # then change the color of the specified position to the specified color
                if capture and return_val:
                    self._board[current_position[0]][current_position[1]] = 'X'

                # Continue to return True/False value from any recursive calls.
                return return_val

        if color == 'white':
            # If a character of the specified color is found, this is a valid capture line. set the return value True
            if self._board[current_position[0]][current_position[1]] == 'O':
                return True

            # If there is a piece of the opposite color, continue to check along that line by calling itself again.
            if self._board[current_position[0]][current_position[1]] == 'X':
                return_val = self.line_capture(color, current_position, direction_offset, capture)

                # If the value to be returned is True, and the capture flag is True,
                # then change the color of the specified position to the specified color
                if capture and return_val:
                    self._board[current_position[0]][current_position[1]] = 'O'

                # Continue to return True/False value from any recursive calls.
                return return_val


"""
"DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"
    Initializing the Player and Othello classes:
        The player is initialized in the Player class init method. 
        The player is initialized as a very basic structure containing private variables for the name and color
        
        the Othello game is initialized in the Othello class init method. 
        The othello board will be initialized as a 10x10 2d array that holds the starting layout of the board.
        two empty players will be initialized, player1 and player2 for use when the players are created
        
        
    Determining how to implement the create_player method:
        Check if there is a Player in player2. 
            If there is, then both players have already been created and a new one cannot be added.
        Validate that the color entered is either 'black' or 'white'
        Check if there is a Player in player1. 
            If there is, validate the color for player1 is different than the color entered, then create the new 
            player in player2
            If there is no player1, create the new player as player1
    
    
    Determining how to implement print_board method
        Loop through each row index in the board.  
            Inside each row loop, loop through the column positions, concatenating them into a string and padding with 
            spaces as necessary
            At the end of each of the rows, print out the concatenated string
    
    
    Determining how to implement return_available_positions method 
        Check each position on the board for a blank space. 
        If a blank space is found, then it needs to be checked for a valid play.
        
        To check for a valid capture, call the check_capture method passing a color and position.
            check_capture uses a submethod, line_capture, which takes in the color and position, along with additional 
            parameters for direction and a capture flag, that will be set false.
            
            line_capture is a recursive function that will:
                Add an offset to the specified position depending on which direction is being checked. 
                If a boundary character or blank space is found, then stop checking this line. It is not a valid capture line. Return False
                If a character of the specified color is found, this is a valid capture line. Return True
                If there is a piece of the opposite color, continue to check along that line by calling itself again.
                Continue to return True/False value from any recursive calls.
            
            If line_capture returns False, check_capture will pass the next direction, repeating until one of the 
            lines returns True or all 8 lines leading from the position have returned False. check_capture will then 
            return True or False back to return_available_positions.
        
        If check_capture returns True, there is at least one valid capture path leading from the current blank space.
        add this to the list of available positions
        
        Once all of the positions on the board have been checked, return the list of available positions.
            
            
        The check_captures method will return true if there are any valid capture paths leading from the specified position.
        If check_captures return
        
    
    Determining how to implement return_winner method 
        Check each position on the board, totaling up black and white tiles
        Once the whole board has been totaled, compare the values
            If the values are the same, print out the message for a tie
            If the black value is higher, check the color of each of the players and get the name of the black player. 
                Print out the message that black has one containing the player name
            Else white is higher. Repeat the process above but for the white player.
    
    
    Determining how to implement make_move method 
        Change the board data at the specified location so that it contains a piece for the specified color
        
        call the capture method. The capture method works very similarly to the check_capture method described above.
        It also uses the submethod line_capture, but sets the capture flag mentioned earlier to True.
        
        In this case, line_capture will add an additional step:
            Add an offset to the specified position depending on which direction is being checked. 
            If a boundary character or blank space is found, then stop checking this line. It is not a valid capture line. Return False
            If a character of the specified color is found, this is a valid capture line. Return True
            If there is a piece of the opposite color, continue to check along that line by calling itself again.
            *If the value to be returned is True, and the capture flag is True, 
                then change the color of the specified position to the specified color
            Continue to return True/False value from any recursive calls.
            
        capture method will continue to call line_capture like this for all 8 directions leading from the piece that was just played.
        
        call the print_board method
    
    
    Determining how to implement play_game method; how to validate a move. Determine how to detect the end of the game.
        validate the move by calling return_available_positions for the player making the move and checking if the 
        position is in the list returned
            If it is not, print out the 'invalid move' message and then the list of valid moves received previously.
        If it is, the move is a valid move. call make_move
        
        To check if the game is over, call return_available_positions for both players. 
        If both lists return empty, then the game is over. Call return_winner then print out the final results

"""
