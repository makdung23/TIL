import sys
sys.stdin = open('input_partsum.txt')

T = int(sys.stdin.readline())

for t in range(1, T+1):
    n, k = map(int, sys.stdin.readline().split())
    subsets = []
    count = 0

    for i in range(1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(j+1)
        subsets.append(subset)

    for subset in subsets : 
        if len(subset) == n:
            sub_sum = 0
            for x in subset:
                sub_sum += x
            if sub_sum == k:
                count += 1

    print('#{} {}'.format(t, count))