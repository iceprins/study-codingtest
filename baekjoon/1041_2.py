import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))
    valid = list()

    if N == 1:
        nums.sort()
        print(sum(nums[:5]))
    else:
        valid.append(min(nums[0], nums[5]))
        valid.append(min(nums[1], nums[4]))
        valid.append(min(nums[2], nums[3]))

        valid.sort()

        min_1 = valid[0]
        min_2 = valid[0] + valid[1]
        min_3 = valid[0] + valid[1] + valid[2]

        face_1 = (N - 2) * (5 * N - 6)
        face_2 = 4 * (2 * N - 3)
        face_3 = 4

        print(min_1 * face_1 + min_2 * face_2 + min_3 * face_3)
