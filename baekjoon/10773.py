import sys

if __name__ == '__main__':
    book = list()
    K = int(sys.stdin.readline().strip())

    for _ in range(K):
        history = int(sys.stdin.readline().strip())
        if history == 0:
            book.pop()
            continue
        book.append(history)

    print(sum(book))