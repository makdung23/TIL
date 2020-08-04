import sys
sys.stdin = open("input_sum.txt")

T = int(sys.stdin.readline())
for t in range(1, T+1):
    n, m = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))

    for i in range(n-m+1):
        now_sum = 0
        for num in num_list[i:i+m]:
            now_sum += num

        if i == 0 :
            max_sum = now_sum
            min_sum = now_sum
        elif now_sum>max_sum :
            max_sum = now_sum
        elif now_sum<min_sum :
            min_sum = now_sum

    print("#{} {}".format(t, max_sum - min_sum))
