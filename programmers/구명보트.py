from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    q = deque(people)

    ans = 0

    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            ans += 1
            q.popleft()
            q.pop()
        else:
            ans += 1
            q.popleft()

    if q:
        ans += 1

    return ans
