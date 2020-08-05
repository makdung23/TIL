import sys
sys.stdin = open("input_daily.txt")

for t in range(1, 11):
    sys.stdin.readline()
    num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(100)]
    
    max_sum = 0
    diag_sum = [0, 0]
    for i in range(100):
        horiz_sum = 0
        vert_sum = 0
        diag_sum[0] += num_list[i][i]
        diag_sum[1] += num_list[99-i][99-i]
        for j in range(100):
            horiz_sum += num_list[i][j]
            vert_sum += num_list[j][i]

        if horiz_sum > vert_sum :
            if horiz_sum > max_sum : 
                max_sum = horiz_sum
        else :
            if vert_sum > max_sum:
                max_sum = vert_sum
    
    if diag_sum[0] > diag_sum[1]:
        if diag_sum[0] > max_sum :
            max_sum = diag_sum[0]
    else :
        if diag_sum[1] > max_sum :
            max_sum = diag_sum[1]

    print('#{} {}'.format(t, max_sum))
