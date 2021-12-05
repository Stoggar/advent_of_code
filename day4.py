with open('./2021_day4.txt', 'r') as f:
    lines = f.readlines()

#with open('./tmp.txt', 'r') as f:
#    lines = f.readlines()

def extract_boards(board_lines):
    if len(board_lines) <= 6:
        return [board_lines]
    return [board_lines[:5]] + extract_boards(board_lines[6:])


class Board:
    def __init__(self, board_str):
        self.board = self._create_board(board_str)
        self.marked = [[0 for j in range(len(self.board[0]))] for i in range(len(self.board))]
        self.player = None
    
    def mark(self, num):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == num:
                    self.marked[i][j] = 1
        return self.win()
    
    def win(self):
        for i, row in enumerate(self.marked):
            if all(row):
                return True
        for col_ix in range(len(self.marked)):
            if all([line[col_ix] for line in self.marked]):
                return True
        return False

    def score(self):
        s = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.marked[i][j]:
                    s += self.board[i][j]
        return s

    @staticmethod
    def _create_board(board_str):
        board = []
        for line in board_str:
            l = line.strip('\n').strip()
            row = [int(i.strip()) for i in l.split()]
            board.append(row)
        return board

    def __str__(self):
        # board
        board_lines = []
        for i, row in enumerate(self.board):
            s = ''
            for j in row:
                s += f'{j:3}'
            if i < len(self.board)-1:
                s += '\n'
            board_lines.append(s)
        # marked
        marked_lines = []
        for i, row in enumerate(self.marked):
            m = ''  
            for j in row:
                m += f'{j:3}'
            if i < len(self.marked)-1:
                m += '\n'
            marked_lines.append(m)
        # append
        total_lines = []
        for i in range(len(board_lines)):
            total_lines.append(board_lines[i].strip('\n') + '   ' + marked_lines[i])
        return ''.join(total_lines)

    def __repr__(self):
        return self.__str__()



draw = [int(i.strip().strip('\n')) for i in lines[0].split(',')]
board_lines = lines[2:]
board_strings = extract_boards(board_lines)
boards = [Board(i) for i in board_strings]
for i in range(len(boards)):
    boards[i].player = i


def play(draw, boards):
    for num_ix, num in enumerate(draw):
        for i, board in enumerate(boards):
            if boards[i].mark(num):
                print(f'board[{i}] Won!')
                return num_ix, i
    return None, None


def loser(draw, boards):
    print(f'loser: draw: \n{draw}\nboards:')
    [print(str(board) + '\n') for board in boards]
    num_ix, winner = play(draw, boards)
    if len(boards) == 1:
        return draw[num_ix], boards[winner].player
    return loser(draw[num_ix:], [board for i, board in enumerate(boards) if not i == winner]) 


num, loser = loser(draw, boards)
score = boards[loser].score()

print(score)
print(num)
print(num*score)



#num_ix, winner = play(draw, boards)
#num = draw[num_ix]
#score = boards[winner].score()
#
#print(score)
#print(num)
#print(num*score)












