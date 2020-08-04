import sys
sys.stdin = open('input_flatten.txt')

for t in range(1, 11):
    dump_num = int(sys.stdin.readline())
    box_nums = list(map(int, sys.stdin.readline().split()))
    max_idx = 0
    min_idx = 0

    while dump_num > 0:
        for i in range(len(box_nums)):
            if box_nums[i]>box_nums[max_idx] : 
                max_idx = i
            if box_nums[i]<box_nums[min_idx]:
                min_idx = i

        if box_nums[max_idx] - box_nums[min_idx] < 2 :
            break
        
        box_nums[max_idx] -= 1
        box_nums[min_idx] += 1
        
        dump_num -= 1

    print("#{} {}".format(t, max(box_nums)-min(box_nums)))
        
