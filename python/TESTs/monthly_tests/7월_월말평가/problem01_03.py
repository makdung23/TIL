import json

def history(movie):
    # movie의 'overview' 키에 대응하는 값에 접근해 줄거리 문자열을 가져오고,
    # in 을 사용해 해당 문자열에 '과거'라는 substring이 포함되어 있는지를 확인한다.

    if '과거' in movie['overview']: # '과거' 문자열이 줄거리에 포함되어 있으면
        return True # True를 반환하고,
    else: # '과거' 문자열이 줄거리에 포함되어 있지 않으면
        return False # False를 반환한다.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False