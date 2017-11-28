import NMM  #This is necessary for the project

BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""

RULES = """
  _   _ _              __  __            _       __  __                 _
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/

    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to
    make mills. When a mill (or mills) is made one opponent's piece can be
    removed from play. In Phase 2 play continues by moving pieces to
    adjacent points.

    The game is ends when a player (the loser) has less than three
    pieces on the board.

"""

MENU = """

    Game commands (first character is a letter, second is a digit):

    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game

"""


def count_mills(board, player):
    """
    takes	 in the current state of the board and one player
    counts how many of the mills are held by the player
    returns the count
    """
    count = 0
    for n in range(16):
        if board.points[board.MILLS[n][0]] == player:
            if board.points[board.MILLS[n][1]] == player:
                if board.points[board.MILLS[n][2]] == player:
                    count += 1
    return count


def place_piece_and_remove_opponents(board, player, destination):
    """
    place	a piece for “player”
    return None
    """
    if destination not in board.points:
        raise RuntimeError("Invalid Placement")
    if board.points[destination] != " ":
        raise RuntimeError("Invalid Placement")
    else:
        before = count_mills(board, player)
        board.assign_piece(player, destination)
        after = count_mills(board, player)
        if after > before:
            print("A mill was formed!")
            print(board)
            remove_piece(board, player)

def move_piece(board, player, origin, destination):
    """
    used to move a piece
    return None
    """
    if destination not in board.points:
        raise RuntimeError("Invalid command: Not a valid point")
    if board.points[origin] != player:
        raise RuntimeError("Invalid command: Origin point does not belong to player")
    if  board.points[destination] != " "  or (destination not in board.ADJACENCY[origin]):
        raise RuntimeError("Invalid command: Not a valid point")
    board.clear_place(origin)
    place_piece_and_remove_opponents(board, player, destination)

def points_not_in_mills(board, player):
    """
    find all points belonging to player that are not in mills
    """
    pnim = set()
    for k,v in board.points.items():
        if v == player:
            for n in range(16):
                if k in board.MILLS[n]:
                    if board.points[board.MILLS[n][0]] == player and board.points[board.MILLS[n][1]] == player and board.points[board.MILLS[n][2]] == player:
                        pnim.add(k)
    result = set()
    for k,v in board.points.items():
        if v == player:
            if k not in pnim:
                result.add(k)
    return result


def placed(board, player):
    """
    Return points where player's pieces have been placed
    """
    p = set()
    for k,v in board.points.items():
        if v == player:
            p.add(k)
    return p

def remove_piece(board, player):
    """
    remove a piece belonging to player from board
    """
    player = get_other_player(player)
    all_in_mill = True
    for k,v in board.points.items():
        if v == player:
            if k in list(points_not_in_mills(board, player)):
                all_in_mill = False
                
    while True:
        try:
            command = input("Remove a piece at :> ").strip().lower()
            if " " in command:
                raise RuntimeError("Invalid command: Not a valid point")
            if command not in list(placed(board, player)):
                raise RuntimeError("Invalid command: Point does not belong to player")
            if command not in list(points_not_in_mills(board, player)) and all_in_mill == False:
                raise RuntimeError("Invalid command: Point is in a mill")
            board.clear_place(command)
            return
        except RuntimeError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
            continue

def is_winner(board, player):
    """
    decide if a game was won
    """
    if len(placed(board, get_other_player(player))) < 3:
        return True
    else:
        return False


def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"


def main():
    #Loop so that we can start over on reset
    while True:
        #Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0  # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent

        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:
                if command == "h":
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                    continue
                elif command == "r":
                    print(RULES)
                    print(MENU)
                    board = NMM.Board()
                    player = "X"
                    placed_count = 0
                else:
                    place_piece_and_remove_opponents(board, player, command)
                    player = get_other_player(player)
                    placed_count += 1

            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            #Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print(
                    "**** Begin Phase 2: Move pieces by specifying two points")
                command = input(
                    "Move a piece (source,destination) :> ").strip().lower()
            print()

        #Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            try:
                if len(command) != 2:
                    raise RuntimeError("Invalid number of points")
                move_piece(board, player, command[0], command[1])
                if is_winner(board, player):
                    print(BANNER)
                    return
                player = get_other_player(player)
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            #Display and reprompt
            print(board)
            #display_board(board)
            print(player + "'s turn!")
            command = input(
                "Move a piece (source,destination) :> ").strip().lower()
            print()

        #If we ever quit we need to return
        if command == 'q':
            return


if __name__ == "__main__":
    main()
