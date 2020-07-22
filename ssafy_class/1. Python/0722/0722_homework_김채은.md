# 0722 Homework

### 서울 4기 1반 김채은

<h5>1. built in 함수 </h5>

​	print, max, min, all, any, dir, list  등. 다음과 같은 구문을 통해 확인 가능하다.

```python
dir(__builtin__)
```



<h5>2. 정중앙 문자</h5>

```python
def get_middle_char(s):
    if len(s) % 2 == 0 : 
        return s[len(s)//2-1 : len(s)//2+1]
    else : return s[len(s)//2]

print(get_middle_char("ssafy"))
print(get_middle_char("coding"))
```



<h5>3. 위치 인자와 키워드 인자</h5>

(4)에서 오류가 난다. 함수 호출에 키워드 인자를 사용할 시에는, 키워드 인자 활용한 뒤에 위치 인자를 활용할 수 없다. 

<h5>4. 나의 반환값은</h5>

없다. my_func 함수는 매개변수를 인자로 받아 연산한 뒤  print를 해주는 함수이고, 반환값이 없다. 

<h5>5. 가변 인자 리스트</h5>

```python
def my_avg(*args):
    result = 0
    for x in args : 
        result += x
    return result/len(args)

print(my_avg(77, 83, 95, 80, 70))
```





