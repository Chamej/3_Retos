from collections import deque


def get_new_state(index1, index2, current_state):
    current_state = list(current_state)
    current_state[index1], current_state[index2] = current_state[index2], current_state[index1]
    return "".join(current_state)


def sliding_puzzle(board):
    graph = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
    init_state = "".join(str(c) for c in board[0] + board[1])
    visited = {init_state}
    queue = deque([[init_state, 0]])
    while queue:
        current_state, step = queue.popleft()
        if current_state == "123450":
            return step

        empty = current_state.find("0")
        for candidate in graph[empty]:
            new_state = get_new_state(empty, candidate, current_state)
            if new_state not in visited:
                queue.append([new_state, step + 1])
                visited.add(new_state)
        print(current_state)
    return -1


print(sliding_puzzle([[1, 2, 3], [0, 4, 5]]))
