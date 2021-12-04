def check_line(line):
    return line == [True, True, True, True, True]


class Card:
    def __init__(self, board):
        self.board = board
        self.found = [[False] * 5 for _ in range(5)]

    def add_if_present(self, num):
        for i, l in enumerate(self.board):
            for j, c in enumerate(l):
                if c == num:
                    self.found[i][j] = True

    def check(self):
        for l in self.found:
            if check_line(l):
                return True
        for l in [[self.found[j][i] for j in range(len(self.found))] for i in range(len(self.found[0])-1,-1,-1)]:
            if check_line(l):
                return True
        return False


text = open('input.txt').readlines()
draw = [int(x) for x in text[0].strip().split(",")]
boards = []
raw_boards = text[2:]

current_board = []
j = 0
for i in range(0, len(raw_boards)):
    line = raw_boards[i]
    if j == 4:
        current_board.append([int(x) for x in line.strip().split(' ') if x.isdigit()])
        boards.append(Card(current_board))
        current_board = []
    elif line == "\n":
        j = -1
    else:
        current_board.append([int(x) for x in line.strip().split(' ') if x.isdigit()])
    j += 1

winner_board = None
last_called = None
for i in draw:
    escape = False
    for board in boards:
        board.add_if_present(i)
        if board.check():
            escape = True
            last_called = i
            winner_board = board
            break
    if escape:
        break

score = 0
for i, cell in enumerate(winner_board.found):
    for j, c in enumerate(cell):
        if not c:
            score += winner_board.board[i][j]
print(f'Score: {score}, Last called: {last_called} Final Score: {score * last_called}')
