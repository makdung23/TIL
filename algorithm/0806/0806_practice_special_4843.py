import sys
sys.stdin = open("input_special.txt")

T = int(sys.stdin.readline())

for t in range(1, T+1):
    sys.stdin.readline()
    num_list = list(map(int, sys.stdin.readline().split()))

    for i in range(len(num_list)-1):
        min_idx = i
        for j in range(i+1, len(num_list)):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    print('#{}'.format(t), end = ' ')
    for i in range(5):
        print('{} '.format(num_list[-i-1]), end = '')
        print('{} '.format(num_list[i]), end = '')

    print()
