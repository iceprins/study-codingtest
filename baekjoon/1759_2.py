import sys

vowel = ['a', 'e', 'i', 'o', 'u']


def dfs(idx, depth):
    if depth == L:
        if len(set(ans) & set(vowel)) >= 1 and len(set(ans) - set(vowel)) >= 2:
            print(''.join(ans).replace(' ', ''))
            return

    for i in range(idx, C):
        ans.append(characters[i])
        dfs(i + 1, depth + 1)
        ans.pop()


if __name__ == '__main__':
    L, C = map(int, sys.stdin.readline().strip().split())
    characters = list(sys.stdin.readline().strip().split())
    ans = []

    characters.sort()

    dfs(0, 0)
