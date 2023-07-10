import sys

consonant = {"q": [1, 1], "w": [1, 2], "e": [1, 3], "r": [1, 4], "t": [1, 5],
             "a": [2, 1], "s": [2, 2], "d": [2, 3], "f": [2, 4], "g": [2, 5],
             "z": [3, 1], "x": [3, 2], "c": [3, 3], "v": [3, 4]}
vowel = {"y": [1, 6], "u": [1, 7], "i": [1, 8], "o": [1, 9], "p": [1, 10],
         "h": [2, 6], "j": [2, 7], "k": [2, 8], "l": [2, 9],
         "b": [3, 5], "n": [3, 6], "m": [3, 7]}


def get_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == '__main__':
    left_init, right_init = map(str, sys.stdin.readline().strip().split())
    input_word = sys.stdin.readline().strip()

    left_from = left_init
    right_from = right_init
    total_time = 0

    for i in range(len(input_word)):
        if input_word[i] == left_from:
            total_time += 1
        elif input_word[i] in consonant:
            total_time += get_dist(consonant[left_from], consonant[input_word[i]])
            total_time += 1
            left_from = input_word[i]
        elif input_word[i] in vowel:
            total_time += get_dist(vowel[right_from], vowel[input_word[i]])
            total_time += 1
            right_from = input_word[i]

    print(total_time)