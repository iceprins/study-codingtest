def solution(enroll, referral, seller, amount):
    answer = []

    parents = dict(zip(enroll, referral))
    stats = {}

    for i in range(len(enroll)):
        stats[enroll[i]] = 0

    def dfs(x, price):
        rest = price * 0.1

        if rest < 1:
            stats[x] += price
            return

        rest = int(rest)
        stats[x] += (price - rest)

        if parents[x] == "-":
            return

        dfs(parents[x], rest)

        return

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)

    for name in enroll:
        answer.append(stats[name])

    return answer
