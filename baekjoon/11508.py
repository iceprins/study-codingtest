import sys

if __name__ == '__main__':
    milk = int(input())
    costs = list()

    for _ in range(milk):
        costs.append(int(sys.stdin.readline().strip()))

    costs.sort(reverse=True)

    total = sum(costs)

    for i in range(2, milk, 3):
        total -= costs[i]

    print(total)
