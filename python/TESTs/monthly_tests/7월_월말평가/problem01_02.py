import json

def title_length(movie):
    # 딕셔너리 movie의 키 'title' 에 대응하는 값에 접근해 영화 제목을 가져오고,
    # 문자열의 길이를 반환하는 파이썬의 내장함수 len()을 사용한다.
    return len(movie['title'])

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # => 4