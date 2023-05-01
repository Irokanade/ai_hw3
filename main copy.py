class Board:
    def __init__(self, rows, cols, board):
        self.rows = rows
        self.cols = cols
        self.board = board
	
    def isGameOver(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 1:
                    return False
        return True
    
    def isLegalMove(self, rowOrCol, index):
        if rowOrCol == 'row':
            for i in range(self.cols):
                if self.board[index][i] == 1:
                    return True
        elif rowOrCol == 'col':
            for i in range(self.rows):
                if self.board[i][index] == 1:
                    return True
        return False
    
    def getLegalMoves(self):
        legalMovesSet = []
        # check all row moves
        for i in range(self.rows):
             if self.isLegalMove('row', i):
                  legalMovesSet.append(['row', i])

        #checl all col moves
        for i in range(self.cols):
             if self.isLegalMove('col', i):
                  legalMovesSet.append(['col', i])

        return legalMovesSet
    
    # move and update board and return score
    def setMove(self, rowOrCol, index):
        score = 0
        if rowOrCol == 'row':
            for i in range(self.cols):
                if self.board[index][i] == 1:
                    self.board[index][i] = 0
                    score += 1

        elif rowOrCol == 'col':
            for i in range(self.rows):
                if self.board[i][index] == 1:
                    self.board[i][index] = 0
                    score += 1

        return score



class Player:
    def __init__(self):
	    self.score = 0
            

class Game:
    def __init__(self, rows, cols, board, noOfPlayers):
        self.board = Board(rows, cols, board)
        self.players = []
        self.noOfPlayers = noOfPlayers
        for i in range(noOfPlayers):
            self.players.append(Player())

    def setMove(self, rowOrCol, index, maximizingPlayer):
        if maximizingPlayer:
            self.players[0].score += self.board.setMove(rowOrCol, index)

        else:
            self.players[1].score += self.board.setMove(rowOrCol, index)

    def isGameOver(self):
         return self.board.isGameOver()



def evaluation(game):
    return game.players[0].score-game.players[1].score
         



def minimax(game, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or game.isGameOver():
        # print(evaluation(game))
        print(game.board.board)
        return ['-1', -1, evaluation(game)]

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in game.board.getLegalMoves():
            game.setMove(child[0], child[1], maximizingPlayer)
            print('depth: ' + str(depth) + ' ' + str(game.board.board))
            eval = []
            eval = minimax(game, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval[2])
            alpha = max(alpha, eval[2])
            if beta <= alpha:
                break
        # print(maxEval)
        # print(game.board.board)
        return [child[0], child[1], maxEval]

    else:
        minEval = float('inf')
        for child in game.board.getLegalMoves():
            game.setMove(child[0], child[1], maximizingPlayer)
            print('depth: ' + str(depth) + ' ' + str(game.board.board))
            eval = []
            eval = minimax(game, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval[2])
            beta = min(beta, eval[2])
            if beta <= alpha:
                break
        # print(minEval)
        # print(game.board.board)
        return [child[0], child[1], minEval]







fin = open("input.txt", "r")    
fout = open("output.txt", "w")

board = []

# input board dimensions
firstline = fin.readline()
tempLine = [int(x) for x in firstline.split(" ")]
rows = tempLine[0]
cols = tempLine[1]

# input board
lines = fin.readlines()
for line in lines:
    tempLine = [int(x) for x in line.split(" ")]
    board.append(tempLine)

myGame = Game(rows, cols, board, 2)

# test print
# print("rows: " + str(rows))
# print("cols: " + str(cols))
# print(board)

print("rows: " + str(myGame.board.rows))
print("cols: " + str(myGame.board.cols))
print(myGame.board.board)

print(myGame.isGameOver())

# minimax
bestMove = []
bestMove = minimax(myGame, 10, float('-inf'), float('inf'), True)

#print result
print('result:')
print(str(bestMove[0]) + str(bestMove[1]))
print(bestMove[2])
print('scores')
print(myGame.players[0].score)
print(myGame.players[1].score)

fin.close()
fout.close()