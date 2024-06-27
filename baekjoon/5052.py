import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        phone_num = []

        for _ in range(n):
            phone_num.append(sys.stdin.readline().strip())

        phone_num.sort()

        for i in range(n - 1):
            if phone_num[i] == phone_num[i + 1][:len(phone_num[i])]:
                print("NO")
                break
        else:
            print("YES")
