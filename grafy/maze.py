from collections import deque

def find_S_and_W(maze):
    S = None
    W = None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                S = (i, j)
            elif cell == 'W':
                W = (i, j)
    return S, W


def find_exit(maze):
    start, end = find_S_and_W(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    directions_symbols = ['d', 'u', 'r', 'l']
    
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        if (x, y) == end:
            break

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] in {'.', 'W'}:
                q.append((nx, ny))
                maze[nx][ny] = directions_symbols[i]

    x, y = end
    if maze[x][y] == 'W':
        print('There is no way out of this maze :(')
    else:
        while (x, y) != start:
            symbol = maze[x][y]
            maze[x][y] = '+'
            
            if symbol == 'u':
                x = x - 1
            elif symbol == 'd':
                x = x + 1
            elif symbol == 'l':
                y = y - 1
            elif symbol == 'r':
                y = y + 1
    
        maze[end[0]][end[1]] = 'W'

        for row in maze:
            print(row)


maze = [
    list("###########.#"),
    list("#S...#....#.#"),
    list("#.#.###.#.#.#"),
    list("#.#.....#..W#"),
    list("#.#########.#"),
    list("############*")
]

maze2 = [
    list("#######"),
    list("#S#.#W#"),
    list("#######")
]

maze3 = [
    list("###########"),
    list("#S..#.....#"),
    list("#.##..###.."),
    list("#....#....#"),
    list("###.#.###.#"),
    list("#....#...W#"),
    list("###########")
]

large_maze = [
    list("####################"),
    list("#S......#..........#"),
    list("#####.#.###.########"),
    list("#.....#.....#......#"),
    list("#.###.#.#####.####.#"),
    list("#...#.#.....#.#....#"),
    list("###.#.###.#.#.#.####"),
    list("#.#.#.....#.#.#....#"),
    list("#.#.#####.#.#.######"),
    list("#.....#...#.#......#"),
    list("######.#.#.#.#######"),
    list("#......#.#...#.....#"),
    list("#.######.#####.###.#"),
    list("#...............#..#"),
    list("#########.#####.#.##"),
    list("#.........#.....#..#"),
    list("#.###########.###.##"),
    list("#.#........#.......#"),
    list("#.#.########.#######"),
    list("#.........W........#"),
    list("####################")
]

find_exit(large_maze)
