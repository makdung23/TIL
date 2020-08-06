import sys
sys.stdin = open("input_daily.txt")

T = int(sys.stdin.readline())

for t in range(1, T+1):
    n, m = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    max_fly = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            fly_sum = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    fly_sum += lst[x][y]
                    
            if fly_sum > max_fly :
                max_fly = fly_sum
    
    print("#{} {}".format(t, max_fly))
