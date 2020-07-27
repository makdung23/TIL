def swap(word):
    # 문자열 word의 모든 문자를 순회하며 ASCII 코드를 활용해 대소문자를 판별한다.
    # 해당 문자가 대문자이면 소문자로, 소문자이면 대문자로 변환해 
    # 새로운 문자열 result에 추가한다. 

    result = '' # result는 빈 문자열로 초기화한다. 
    for letter in word: # word의 모든 문자를 순회하며,
        if ord(letter) in range(65, 91): # 해당 문자가 대문자이면
            result += chr(ord(letter)+32) # ASCII 코드 값에 32를 더해 소문자로 변환한 뒤 result 문자열에 concatenate하고
        elif ord(letter) in range(97, 123): # 해당 문자가 소문자이면
            result += chr(ord(letter)-32) # ASCII 코드 값에 32를 빼 대문자로 변환한 뒤 result 문자열에 concatenate한다.
        else : # 알파벳이 아닌 그 외의 문자인 경우에는
            result += letter # 해당 문자를 그대로 result 문자열에 concatenate한다.
    return result # 변환된 문자열 result를 반환한다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'