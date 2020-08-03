for t in range(1, 11):
    build_num = int(input())
    buildings = list(map(int, input().split()))
    count = 0

    for i in range(2, build_num-1):
        if buildings[i] <= buildings[i+1] or buildings[i] <= buildings[i-1]:
            continue
        elif buildings[i] > buildings[i+2] and buildings[i] > buildings[i-2] :
            count += (buildings[i] - max(buildings[i-2:i]+buildings[i+1:i+3]))

    print(f'#{t} {count}')