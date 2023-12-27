if __name__ == '__main__':
    N = int(input())

    bundle_of_five = N // 5

    while True:
        rest = N - 5 * bundle_of_five
        if rest == 0:
            print(bundle_of_five)
            break
        if rest < 3:
            if bundle_of_five == 0:
                print(-1)
                break
            bundle_of_five -= 1
        else:
            if rest % 3 == 0:
                print(bundle_of_five + rest // 3)
                break
            if bundle_of_five == 0:
                print(-1)
                break
            bundle_of_five -= 1