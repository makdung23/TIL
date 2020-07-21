# 200721 workshop

### 서울 4기 1반 김채은

<h5> 1. 간단한 N의 약수 </h5>

```python
N = int(input())
for i in range(1, N+1):
    if N%i == 0 : 
        print(i, end =" ")
```

<h5> 2. 중간값 찾기 </h5>

```python
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]
print(sorted(numbers)[len(numbers)//2])
```

<h5>3. 계단 만들기</h5>

```python
number = int(input())
for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
```

<h5>4. 구구단을 외자, 구구단을 외자!</h5>

```python
for i in range(2, 10) :
    print(f"------ [{i} 단] ------")
    for j in range(1, 10) :
        print(f'{i} X {j} = {i*j}')
```

