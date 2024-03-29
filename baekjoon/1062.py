# 백트래킹 활용
import sys


def dfs(start, cnt):
    global ans

    if cnt == K - 5:
        tmp = 0
        for word in words:
            is_contain = True
            for char in word:
                if not check[ord(char) - ord('a')]:
                    is_contain = False
                    break

            if is_contain:
                tmp += 1

        ans = max(ans, tmp)
        return

    for i in range(start, 26):
        if not check[i]:
            check[i] = True
            dfs(i, cnt + 1)
            check[i] = False


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    words = [set(sys.stdin.readline().strip()) for _ in range(N)]
    check = [False] * 26
    ans = 0

    for c in ('a', 'c', 'i', 'n', 't'):
        check[ord(c) - ord('a')] = True

    if K < 5:
        print(0)
    elif K == 26:
        print(N)
    else:
        dfs(0, 0)
        print(ans)

# 비트마스킹 활용
import sys
from itertools import combinations


def word_to_bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().strip().split())
    words = [set(sys.stdin.readline().strip()) for _ in range(N)]
    bits = list(map(word_to_bit, words))
    base_bit = word_to_bit('acint')

    if K < 5:
        print(0)
    elif K == 26:
        print(N)
    else:
        alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]  # a, c, i, n, t를 제외한 알파벳
        answer = 0
        for combination in combinations(alphabet, K - 5):
            know_bit = sum(combination) | base_bit  # 기본적으로 배우는 알파벳과 추가로 배우는 알파벳을 합치는 과정
            count = 0
            for bit in bits:  # 주어진 단어들
                if bit & know_bit == bit:  # 단어의 알파벳을 모두 읽을 수 있는 경우
                    count += 1
            answer = max(answer, count)
        print(answer)
