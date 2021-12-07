
class BingoNumber:
    def __init__(self, number, marked):
        self.number = number
        self.marked = marked

    def mark(self):
        self.marked = True


class BingoBoard:
    def __init__(self, row_size, numbers):
        self.row_size = row_size
        self.number_of_rows = len(numbers) // row_size
        self.board_numbers = [BingoNumber(number, False) for number in numbers]
        self.last_marked = None
    
    def mark_number(self, number):
        for board_number in self.board_numbers:
            if (board_number.number == number):
                board_number.mark()
                self.last_marked = board_number
                return

    def is_winner(self):
        for r in range(self.number_of_rows):
            c = 0
            while c < self.row_size and self.board_numbers[r * self.row_size + c].marked:
                c += 1
            if c == self.row_size:
                return True
        
        for c in range(self.row_size):
            r = 0
            while r < self.number_of_rows and self.board_numbers[r * self.row_size + c].marked:
                r += 1
            if r == self.number_of_rows:
                return True

        return False

    def score(self):
        return sum(board_number.number for board_number in self.board_numbers if not board_number.marked) * int(self.last_marked.number or 0)


with open('input.txt', 'r') as input:
    draw = [int(n) for n in input.readline().split(',')]
    boards = []
    board_numbers = []
    for line in input.readlines():
        if not line.strip():
            if board_numbers:
                boards.append(BingoBoard(5, board_numbers))
                board_numbers = []
        else:
            board_numbers += [int(n) for n in line.split()]
    if board_numbers:
        boards.append(BingoBoard(5, board_numbers))

for draw_number in draw:
    for board in boards:
        board.mark_number(draw_number)
        if (board.is_winner()):
            print('solution', board.score())
            exit(1)

