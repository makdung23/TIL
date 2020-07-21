# 0721 homework 

### 서울 4기 1반 김채은

<h5> 1. Mutable & Immutabe </h5>

* Mutable : List , Set, Dictionary
* Immutable : String, Tuple, Range

<h5> 2. 홀수만 담기 </h5>

```python
odd_list = list(range(1, 51, 2))
```

<h5>3. Dictionary 만들기</h5>

```python
student_info = {"김채은": 24, "신누리": 24, "김한빈": 28, "황경서": 27, "이종하": 27}
```

<h5>4. 반복문으로 네모 출력 </h5> 

```python
n = 5; m = 9
for i in range(n):
    for j in range(m):
        print("*", end ="")
    print()
```

<h5>5. 조건 표현식</h5>

```python
temp = 36.5
print("입실 불가") if temp >= 37.5 else print("입실 가능")
```

<h5>6. 평균 구하기</h5>

 ```python
scores = [80, 89, 99, 83]
print(f"평균 : {sum(scores)/len(scores)}")
 ```

