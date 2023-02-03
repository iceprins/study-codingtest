import sys

coin_type, coin_sum = map(int, sys.stdin.readline().split())

coins = list()
for _ in range(coin_type):
    coins.append(int(sys.stdin.readline().strip()))

result = 0
for i in range(coin_type):
    if coins[-i-1] <= coin_sum:
        temp = (coin_sum//coins[-i-1])
        coin_sum -= temp * coins[-i-1]
        result += temp

print(result)