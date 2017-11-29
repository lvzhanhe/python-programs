## Nine Men’s Morris

Nine Men’s Morris is a mill-forming board game for two people that plays like a cross between Tic-Tac-Toe, Checkers, and Go. We will be writing a program that allows for the game to be played.

### Features
```
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

	Game commands (first character is a letter, second is a digit):

	xx        Place piece at point xx (only valid during Phase 1 of game)
	xx yy     Move piece from point xx to point yy (only valid during Phase 2)
	R         Restart the game
	H         Display this menu of commands
	Q         Quit the game
```