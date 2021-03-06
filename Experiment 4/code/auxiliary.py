def get_children(board):
    space_index = [(board.index(row), row.index(0)) for row in board if 0 in row][0]

    # move up
    list_board = [list(row) for row in board]
    if space_index[0] > 0:
        list_board[space_index[0]-1][space_index[1]], list_board[space_index[0]][space_index[1]] = \
            list_board[space_index[0]][space_index[1]], list_board[space_index[0]-1][space_index[1]]
        child = tuple(tuple(row) for row in list_board)
        yield child

    # move down
    list_board = [list(row) for row in board]
    if space_index[0] < 2:
        list_board[space_index[0]][space_index[1]], list_board[space_index[0]+1][space_index[1]] = \
            list_board[space_index[0]+1][space_index[1]], list_board[space_index[0]][space_index[1]]
        child = tuple(tuple(row) for row in list_board)
        yield child

    # move left
    list_board = [list(row) for row in board]
    if space_index[1] > 0:
        list_board[space_index[0]][space_index[1]-1], list_board[space_index[0]][space_index[1]] = \
            list_board[space_index[0]][space_index[1]], list_board[space_index[0]][space_index[1]-1]
        child = tuple(tuple(row) for row in list_board)
        yield child

    # move right
    list_board = [list(row) for row in board]
    if space_index[1] < 2:
        list_board[space_index[0]][space_index[1]], list_board[space_index[0]][space_index[1]+1] = \
            list_board[space_index[0]][space_index[1]+1], list_board[space_index[0]][space_index[1]]
        child = tuple(tuple(row) for row in list_board)
        yield child


def construct_path(come_from, state):
    path = list()
    while state in come_from:
        path.append(state)
        state = come_from[state]
    path.reverse()
    return path


def print_path(path):
    for index, board in enumerate(path):
        print('Step %d: ' % index)
        for row in board:
            print(row[0] if row[0] != 0 else ' ',
                  row[1] if row[1] != 0 else ' ',
                  row[2] if row[2] != 0 else ' ')
        print()


def path_to_str(path):
    string = ""
    for index, board in enumerate(path):
        string += 'Step %d: \n' % index
        for row in board:
            string += (str(row[0]) if row[0] != 0 else ' ') + ' '
            string += (str(row[1]) if row[1] != 0 else ' ') + ' '
            string += (str(row[2]) if row[2] != 0 else ' ') + '\n'
        string += '\n'
    return string
