def caesar(word, n):
    # 문자열 word의 모든 문자를 순회하며 
    # 각 문자의 ASCII 코드에 n을 더한 값에 해당하는 문자를 새로운 문자열 result에 추가한다.
    # 단, 대소문자 여부는 바뀌지 않도록 하며 
    # 문자를 n만큼 밀었을 때 알파벳의 범위를 벗어나면 다시 a/A로 돌아와 벗어난 만큼의 거리를 다시 더하도록 한다.

    result = '' # result는 빈 문자열로 초기화한다. 
    for letter in word: # 문자열 word의 모든 문자를 순회하며, 
        if ord(letter) in range(65, 91): # 해당 문자가 대문자인 경우
            if ord(letter)+n not in range(65, 91) : # 해당문자의 ASCII 코드에 n을 더한 값이 알파벳 대문자 코드의 범위를 벗어나면
                result += chr(65 + (ord(letter)+n-65)%26) # 벗어난 만큼의 값을 다시 대문자 A를 기준으로 더한 뒤 문자로 변환해 result에 concatenate한다.
            else : # n을 더한 값이 알파벳 대문자 코드의 범위를 벗어나지 않으면
                result += chr(ord(letter)+n) # n을 더한 코드 값을 문자로 변환해 result에 concatenate한다

        elif ord(letter) in range(97, 123): # 해당 문자가 소문자인 경우에도, 소문자를 기준으로 위의 case와 동일하게 수행한다. 
            if ord(letter)+n not in range(97, 123):
                result += chr(97 + (ord(letter)+n-97) %26)
            else :
                result += chr(ord(letter) + n)
    return result # 새롭게 변환된 문자열 result를 반환한다. 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'