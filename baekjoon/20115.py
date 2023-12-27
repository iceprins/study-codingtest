import sys

if __name__ == '__main__':
    drinks = int(sys.stdin.readline().strip())

    drink_capacity = list(map(int, sys.stdin.readline().strip().split()))
    drink_capacity.sort(reverse=True)

    first_drink = drink_capacity.pop(0)
    max_drink = first_drink + 0.5 * sum(drink_capacity)

    print(max_drink)