import sys
from itertools import combinations

if __name__ == '__main__':
    L, C = map(int, sys.stdin.readline().strip().split())
    character = list(sys.stdin.readline().strip().split())
    vowel = ['a', 'e', 'i', 'o', 'u']
    character.sort()

    cand = list(combinations(character, L))

    for elem in cand:
        tmp = ""
        if set(elem) == set(elem) - set(vowel):
            continue
        if len(set(elem) - set(vowel)) < 2:
            continue
        for alpha in elem:
            tmp += alpha
        print(tmp)
