import sys

word_num = int(sys.stdin.readline())
result = word_num

for _ in range(word_num):
    word = sys.stdin.readline()
    for i in range(len(word) - 1):
        if word[i] != word[i+1] and word[i] in word[i+1:]:
            result -= 1
            break
print(result)