import math

class Sudoku_X:
    def __init__(self,board) -> None:
        self.box_divider = int(math.sqrt(len(board[0])))
        self.max_num = int(len(board))
        self.board = board



    def print_board(self, board):
        for row in range(len(board)):
            if row % self.box_divider == 0:
                #printing a divider for every third row
                print("________ " * self.box_divider + "\n")
            for column in range(len(board[row])):
                #seperating the numbers into 3x3 squares
                if column % self.box_divider == 0 and column!= 0:
                    print(" | ", end="")

                #checking if at the beginning
                if column == 0:
                    print("| ", end="")

                if column == self.max_num - 1:
                    # \n to get to next line
                    print(str(board[row][column]) + " |")
                else:
                    print(str(board[row][column]) + " ", end="")
                
            if row == self.max_num - 1:
                print("________ " * self.box_divider )


    def find_empty_square(self, board):
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 0:
                    return (row,column)
        return None

                
    def validate(self, board, num, position):
        row_lenght = len(board[0])
        #checking the row
        for column in range(row_lenght):
            # check each each column in row to make sure number input is not repeated
            # excludes position we put num in (position[1] != column)
            if board[position[0]][column] == num and position[1] != column:
                # number was found in a position other than input
                return False
        
        # checking each row in column
        for row in range(len(board)):
            if board[row][position[1]] == num and position[0] != row:
                # number was found in a position other than input
                return False
            
        # check boxes
        xplot_box = position[1] // self.box_divider
        yplot_box = position[0] // self.box_divider

        for row in range(yplot_box * self.box_divider, (yplot_box * self.box_divider) + self.box_divider):
            for column in range(xplot_box * self.box_divider, (xplot_box) * self.box_divider + self.box_divider):
                if board[row][column] == num and (row,column) != position:
                    return False
                
        return True

    def backtracking(self, board):

        if float(math.sqrt(len(board[0]))).is_integer() == False:
            print("\nBoard is not compatible with Sudoku Rules.\n")
            return False
        
        find = self.find_empty_square(board)
        if not find:
            self.print_board(board)
            return True
        else:
            row, column = find

        for num in range(1, self.max_num + 1):
            if self.validate(board, num, (row, column)):
                board[row][column] = num

                if self.backtracking(board):
                    return True
                
                board[row][column] = 0
        
        return False


# Test Cases

# board4 = [
#     [0, 0, 4, 0],
#     [2, 0, 0, 1],
#     [1, 0, 0, 4],
#     [0, 2, 0, 0]
# ]

# sudoku_game4 = Sudoku_X(board4)
# sudoku_game4.backtracking(board4)

# empty_9x9_board = [
#     [0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]

# sudoku_game9_empty = Sudoku_X(empty_9x9_board)
# sudoku_game9_empty.backtracking(empty_9x9_board)


# board9 = [
#     [0,2,0,0,8,0,0,7,0],
#     [4,7,0,0,0,9,0,0,0],
#     [0,0,0,0,0,3,5,2,0],
#     [0,9,2,3,0,0,1,0,0],
#     [0,1,0,0,7,0,0,3,5],
#     [0,0,7,9,0,5,6,0,0],
#     [7,0,4,0,0,0,2,0,6],
#     [0,0,0,6,3,4,0,0,0],
#     [6,0,0,0,9,0,0,5,3]
# ]

# sudoku_game9 = Sudoku_X(board9)
# sudoku_game9.backtracking(board9)

# board1 = [[0]]

# sudoku_game1 = Sudoku_X(board1)
# sudoku_game1.backtracking(board1)



# board16 = [
#     [ 0,  0,  0, 13,  0,  0,  0,  1, 16,  0,  0,  0, 14,  0,  0,  0],
#     [14,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9],
#     [ 0,  0,  0,  0,  0,  3,  0, 15,  0,  8,  0,  0,  0,  0,  0,  0],
#     [ 0,  0, 11,  0,  0,  0,  9,  0,  0,  0,  0,  4,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0, 14,  0,  0,  0,  7,  0,  0,  0,  0],
#     [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0, 12,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0,  0],
#     [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
#     [ 5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [ 0,  0,  0, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
# ]

# sudoku_game16 = Sudoku_X(board16)
# sudoku_game16.backtracking(board16)
# print(sudoku_game16.board)

# inspiration taken from Tech With Tim on Youtube