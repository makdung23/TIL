import sys
sys.stdin = open("input_minmax.txt")

T = int(sys.stdin.readline())
for t in range(1, T+1):
    sys.stdin.readline()
    num_list = list(map(int, sys.stdin.readline().split()))

    max_num = min_num = num_list[0]

    for num in num_list[1:]:
        if num > max_num :
            max_num = num
        elif num < min_num :
            min_num = num

    print("#{} {}".format(t, max_num-min_num))