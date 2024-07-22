import random

def generate_board(size, mines) -> list[list[int]]:
    board = [[0 for _ in range(size[0])] for _ in range(size[1])]

    mines_idx = random.sample(range(size[0] * size[1]), mines)

    for i in range(size[0]*size[1]):
        board[i//size[0]][i%size[0]] = 0 if i not in mines_idx else 1

    return board, mines_idx

def generate_neighbor_board(size, mines):
    board, mines_idx = generate_board(size, mines)
    size = len(board[0]), len(board)
    board.insert(0, [0 for _ in range(size[0]+2)])
    board.append([0 for _ in range(size[0]+2)])

    for i in range(1, size[1]+1):
        board[i].insert(0, 0)
        board[i].append(0)

    n_board = [[-1 for _ in range(size[0])] for _ in range(size[1])]

    for y in range(1, size[1]+1):
        for x in range(1, size[0]+1):
            if board[y][x] != 1:
                n_board[y-1][x-1] = board[y-1][x-1] + board[y-1][x] + board[y-1][x+1] + board[y][x-1] + board[y][x+1] + board[y+1][x-1] + board[y+1][x] + board[y+1][x+1]

    mines_idx = [(i%size[0], i//size[0]) for i in mines_idx]

    return n_board, mines_idx


# import utils
# board = generate_board(utils.WINDOW_SIZES[2], utils.WINDOW_MINES_COUNT[2])
# n_board = generate_neighbor_board(board)

# print(*board, sep="\n")
# print(*n_board, sep="\n")


