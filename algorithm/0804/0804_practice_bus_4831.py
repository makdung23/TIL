import sys
sys.stdin = open("input_bus.txt")

T = int(sys.stdin.readline())
for t in range(1, T+1):
    k, n, _ = map(int, sys.stdin.readline().split())
    charge_list = list(map(int, sys.stdin.readline().split()))
    stations = [0 if i not in charge_list else 1 for i in range(1, n + 1)]

    count = 0
    charged = k

    for i in range(len(stations)) :
        charged -= 1
        if i == len(stations)-1:
            pass
        elif charged <= 0 and stations[i] == 0:
            count = 0
            break
        elif stations[i] == 1 and charged == 0:
            count += 1
            charged = k
        elif stations[i] == 1 and 1 not in stations[i+1: i+charged+1] and i+charged+1<len(stations):
            count += 1
            charged = k

    print("#{} {}".format(t, count))