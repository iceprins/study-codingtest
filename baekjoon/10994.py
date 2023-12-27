import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    for i in range(2*(N-1)):
        if i % 2 == 0:
            for _ in range(i//2):
                print("* ", end='')
            for _ in range(1+4*(N-1-i//2)):
                print("*", end='')
            for _ in range(i//2):
                print(" *", end='')
            print()
        else:
            for _ in range((i+1)//2):
                print("* ", end='')
            for _ in range(1+4*(N-1-(i+1)//2)):
                print(" ", end='')
            for _ in range((i+1)//2):
                print(" *", end='')
            print()

    for _ in range(N - 1):
        print("* ", end='')
    print("*", end='')
    for _ in range(N - 1):
        print(" *", end='')
    print()

    for i in range(1 + 2*(N-1), 1+4*(N-1)):
        if i % 2 == 0:
            for _ in range(((4*(N-1))-i)//2):
                print("* ", end='')
            for _ in range(1 + 4*(N-((4*(N-1))-i)//2-1)):
                print("*", end='')
            for _ in range(((4*(N-1))-i)//2):
                print(" *", end='')
            print()
        else:
            for _ in range((1+4*(N-1)-i)//2):
                print("* ", end='')
            for _ in range(1+4*(N-((1+4*(N-1)-i)//2)-1)):
                print(" ", end='')
            for _ in range((1+4*(N-1)-i)//2):
                print(" *", end='')
            print()