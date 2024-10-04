def solution(n, costs):
    costs.sort(key=lambda x: (x[2], x[0]))
    connected = {costs[0][0]}
    cnt = 0

    while len(connected) != n:
        for cost in costs:
            if cost[0] in connected and cost[1] in connected:
                continue
            if cost[0] in connected or cost[1] in connected:
                connected.update([cost[0], cost[1]])
                cnt += cost[2]
                break

    return cnt


# 241004 풀이
def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]

    def union(x, y):
        nonlocal parents
        x = find(x)
        y = find(y)

        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    def find(x):
        nonlocal parents
        if x != parents[x]:
            parents[x] = find(parents[x])

        return parents[x]

    for i in range(len(costs)):
        a, b, cost = costs[i]
        if find(a) == find(b):
            continue
        union(a, b)
        answer += cost

    return answer