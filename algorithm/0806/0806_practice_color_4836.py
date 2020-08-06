import sys
sys.stdin = open("input_color.txt")

T = int(sys.stdin.readline())

for t in range(1, T+1):
    box_num = int(sys.stdin.readline())
    board = [[0 for _ in range(10)] for _ in range(10)]
    
    for _ in range(box_num):
        left_x, left_y, right_x, right_y, color = map(int, sys.stdin.readline().split())
        
        for x in range(left_x, right_x+1):
            for y in range(left_y, right_y+1):
                if board[x][y] == 0: #내가 처음 들어오는 거면 내 컬러 인덱스로
                    board[x][y] = color
                elif board[x][y] == color: #나랑 같은 색깔 있었으면
                    pass
                else:
                    board[x][y] = 3
    
    purple_count = 0
    
    for line in board :
        for n in line:
            if n==3 :
                purple_count += 1
            
    print('#{} {}'.format(t, purple_count))