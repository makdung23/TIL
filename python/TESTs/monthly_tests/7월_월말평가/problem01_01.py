import json

def over(movie):
    # 딕셔너리 movie의 키 'user_rating'에 대응하는 값이 영화 평점 정보를 갖고 있으므로
    # movie['user_rating']의 방식으로 정보에 접근한다.

    if movie['user_rating']>=8: # 평점이 8 이상인 경우에는 
        return True # True를 반환하고,
    else : # 그 외의 경우에는 
        return False # False를 반환한다. 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True