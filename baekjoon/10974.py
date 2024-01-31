from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    num = ""
    for i in range(1, N + 1):
        num += str(i)

    for i in permutations(num, N):
        print(*i)
