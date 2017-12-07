class GoPiece(object):
    ''' It represents black or white pieces used in the game.'''
    def __init__(self,color = 'black'):
        '''Creates a Gomoku piece'''
        if (color != 'black') and (color != 'white'):
            raise MyError('Wrong color.')
        self.__color = color
    
    def __str__(self):
        '''Display color'''
        if self.__color == 'black':
            return ' ● '
        elif self.__color == 'white':
            return ' ○ '
    
    def get_color(self):
        '''Returns the color of the piece'''
        if self.__color == 'black':
            return 'black'
        elif self.__color == 'white':
            return 'white'
            
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    '''Gomoku Class'''
    def __init__(self,board_size=15,win_count=5,current_player='black'):
        if type(board_size) != int:
            raise ValueError()
        self.__board_size = board_size
        if type(win_count) != int:
            raise ValueError()
        self.__win_count = win_count
        if (current_player != 'black') and (current_player != 'white'):
            raise MyError('Wrong color.')
        self.__current_player = current_player
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]  
            
    def assign_piece(self,piece,row,col):
        '''places the piece at the specified position on the game board'''
        if row > self.__board_size or col > self.__board_size:
            raise MyError('Invalid position.')
        if self.__go_board[row-1][col-1] != ' - ':
            raise MyError('Position is occupied.')
        self.__go_board[row-1][col-1] = str(piece)

    def get_current_player(self):
        ''' returns the current player'''
        if self.__current_player == 'black':
            return 'black'
        if self.__current_player == 'white':
            return 'white'
    
    def switch_current_player(self):
        ''' returns the ‘other’ player as a string'''
        if self.__current_player == 'black':
            self.__current_player = 'white'
            return 'white'
        if self.__current_player == 'white':
            self.__current_player = 'black'
            return 'black'
        
    def __str__(self):
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
        
    def current_player_is_winner(self):
        ''' check if the current player wins'''
        piece = GoPiece(self.__current_player)
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__go_board[i][j] == str(piece):
                    if j + self.__win_count <= self.__board_size:
                        result = True
                        for x in range (self.__win_count):
                            if self.__go_board[i][j+x] != str(piece):
                                result = False
                        if result == True:
                            return True
                    if i + self.__win_count <= self.__board_size:
                        result = True
                        for x in range (self.__win_count):
                            if self.__go_board[i+x][j] != str(piece):
                                result = False
                        if result == True:
                            return True
                    if i + self.__win_count <= self.__board_size and j + self.__win_count <= self.__board_size:
                        result = True
                        for x in range (self.__win_count):
                            if self.__go_board[i+x][j+x] != str(piece):
                                result = False
                        if result == True:
                            return True
                    if i + self.__win_count <= self.__board_size and j + 1 >= self.__win_count:
                        result = True
                        for x in range (self.__win_count):
                            if self.__go_board[i+x][j-x] != str(piece):
                                result = False
                        if result == True:
                            return True
        return False
                        
def main():

    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        try: 
            if len(play_list) != 2:
                raise MyError("Incorrect input.")
            if not (play_list[0].isdigit() and play_list[1].isdigit()) and '-' not in play_list[0] and '-' not in play_list[1]:
                raise MyError("Incorrect input.")
            piece = GoPiece(board.get_current_player())
            board.assign_piece(piece,int(play_list[0]),int(play_list[1]))
            if_win = board.current_player_is_winner()
        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
            print(board)            
            play = input("Input a row then column separated by a comma (q to quit): ")
            continue            
        
        if if_win:
            print(board)
            print("{} Wins!".format(board.get_current_player()))
            return            
        else:
            board.switch_current_player()
            print(board)            
            play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()
