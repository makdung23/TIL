def dec_to_bin(n):
    if n==0 or n==1 : # n이 0이거나 1인 경우에는 
        return str(n) # 문자열로 변환만 한 뒤 반환한다.
        # base case로, 종료조건으로 활용된다. 
    else :
        return dec_to_bin(n//2) + str(n%2) 
        # 그 외의 경우에는, n을 2로 나눈 몫에 대하여 dec_to_bin 함수를 다시 실행하고, 
        # 그 결과값 뒤에 n을 2로 나눈 나머지를 문자열로 변환해 concatenate해 반환한다. 

    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'