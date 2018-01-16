from evaluate import heuristic_value
import copy


def is_terminal(node):
    for i in range(15):
        if node[i].count('0') > 0:
            return False
    return True


def generate_child(node, player):
    for i in range(8):
        for j in range(8):
            if node[7-i][7-j] == '0':
                child = copy.deepcopy(node)
                child[7-i][7-j] = str(player)
                yield child, (8 - i, 8 - j)
            if j < 7 and node[7-i][7+j+1] == '0':
                child = copy.deepcopy(node)
                child[7-i][7+j+1] = str(player)
                yield child, (8 - i, 8 + j + 1)
            if i < 7 and node[7+i+1][7-j] == '0':
                child = copy.deepcopy(node)
                child[7+i+1][7-j] = str(player)
                yield child, (8 + i + 1, 8 - j)
            if i < 7 and j < 7 and node[7+i+1][7+j+1] == '0':
                child = copy.deepcopy(node)
                child[7+i+1][7+j+1] = str(player)
                yield child, (8 + i + 1, 8 + j + 1)


def alpha_beta(node, pos_x, pos_y, depth, alpha, beta, maximizing_player, current):
    if depth == 0 or is_terminal(node):
        return heuristic_value(node, pos_x, pos_y, maximizing_player), (pos_x, pos_y)
    if maximizing_player == current:
        v = -float('inf')
        choice = None
        for child in generate_child(node, maximizing_player):
            new_v, new_choice = alpha_beta(child[0], child[1][0], child[1][1], depth - 1, alpha, beta, maximizing_player,
                                           2 if current == 1 else 1)
            if new_v > v:
                v = new_v
                choice = new_choice
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v, choice
    else:
        v = float('inf')
        choice = None
        for child in generate_child(node, maximizing_player):
            new_v, new_choice = alpha_beta(child[0], child[1][0], child[1][1], depth - 1, alpha, beta, maximizing_player,
                                           1 if current == 2 else 2)
            if new_v < v:
                v = new_v
                choice = new_choice
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v, choice
