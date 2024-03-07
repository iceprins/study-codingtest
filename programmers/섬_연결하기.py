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
