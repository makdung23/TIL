import sys
sys.stdin = open('input_binary.txt')

T = int(sys.stdin.readline())

for t in range(1, T+1):
    total_page, page_A, page_B = map(int, sys.stdin.readline().split())
    left_A, right_A, left_B, right_B = (1, total_page, 1, total_page)
    win = ''
    
    while True:
        next_A = int((left_A + right_A)/2)
        next_B = int((left_B + right_B)/2)

        if next_A == page_A and next_B != page_B:
            win = 'A'
            break
        elif next_A != page_A and next_B == page_B:
            win = 'B'
            break
        elif next_A == page_A and next_B == page_B:
            win = '0'
            break

        if next_A > page_A:
            right_A = next_A
        else : 
            left_A = next_A

        if next_B > page_B:
            right_B = next_B
        else : 
            left_B = next_B

    print('#{} {}'.format(t, win))
            
        