import sys

if __name__ == '__main__':
    city = int(input())
    road = list(map(int, sys.stdin.readline().strip().split()))
    petrol = list(map(int, sys.stdin.readline().strip().split()))

    final_cost = 0

    min_cost = petrol[0]
    for i in range(city - 1):
        if petrol[i] < min_cost:
            min_cost = petrol[i]
        final_cost += min_cost * road[i]

    print(final_cost)