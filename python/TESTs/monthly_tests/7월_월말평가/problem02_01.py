import json

def check(data):
    # 체온이 3번 연속으로 37.5도 이상인 경우라면,
    # 3번 중 2번은 무조건 같은 날의 오전/오후 체온에 해당하며
    # 나머지 1번은 전날 오후 혹은 다음날 오전의 체온이다. 

    for i in range(len(data)): # data 리스트의 모든 내부리스트를 순회한다.
        if data[i][0]>=37.5 and data[i][1]>=37.5 : # 만약 해당 내부리스트의 모든 값, 즉 해당 날짜의 오전/오후 체온이 모두 37.5도 이상인 경우,
            if data[i-1][1]>=37.5 or data[i+1][0]>=37.5: # 전날 오후 혹은 다음날 오전의 체온 또한 37.5도 이상이라면
                return True # True를 반환하고 함수를 종료한다.
    return False # 위의 반복문에서 단 한번도 return문에 접근하지 않았다면 False를 반환한다.
                

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True