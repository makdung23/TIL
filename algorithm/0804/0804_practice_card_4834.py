import sys
sys.stdin = open("input_card.txt")

T = int(sys.stdin.readline())
for t in range(1, T+1):
    input()
    card_list = list(map(int, list(input())))
    card_dict = {}

    for card in card_list :
        if card in card_dict :
            card_dict[card] += 1
        else :
            card_dict[card] = 1

    max_card = card_list[0]
    for card in card_dict :
        if card_dict[card] > card_dict.get(max_card) :
            max_card = card
        elif card_dict[card] == card_dict.get(max_card) :
            if max_card < card :
                max_card = card

    print('#{} {} {}'.format(t, max_card, card_dict[max_card]))