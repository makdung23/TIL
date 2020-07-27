import json

def rotate(data):
    result = {} # result 변수는 빈 딕셔너리로 초기화한다. 

    # 이중리스트 data의 모든 값에 접근하여
    # 모든 내부리스트의 0번째 인덱스값을 모은 리스트는 result의 키 'am'에,
    # 모든 내부리스트의 1번째 인덱스값을 모은 리스트는 result의 키 'pm'에 대응하는 값에 할당한다. 
    # data의 모든 내부리스트를 순회하는 데에는 list comprehension을 활용한다.
    result['am'] = [x[0] for x in data]
    result['pm'] = [x[1] for x in data]
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
