import sys

graph = list()
num = list()


def dfs(x, y):
    if x < 0 or x >= map_size or y < 0 or y >= map_size:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


if __name__ == '__main__':
    map_size = int(sys.stdin.readline().strip())

    for _ in range(map_size):
        row = sys.stdin.readline().strip()
        temp = list()
        for i in range(map_size):
            temp.append(int(row[i]))
        graph.append(temp)

    count = 0
    result = 0
    for i in range(map_size):
        for j in range(map_size):
            if dfs(i, j):
                num.append(count)
                result += 1
                count = 0

    print(result)

    num.sort()
    for elem in num:
        print(elem)