# 200721 practice2

### 서울 4기 1반 김채은

#### 1. 더블더블

```python
number = int(input())
result = 0

for i in range(1, number+1) : 
    if i%2 == 0 : result += 3*i
    else : result += 2*i

print(result)
```

#### 2. 간단한 소수 판별 1

```python
number = int(input())
isprime = True

for i in range(2, number) : 
    if number%i == 0 : 
        isprime = False; break

print('Y') if isprime else print('N')
```

#### 3. 간단한 소수 판별 2

```python
numbers = [26, 39, 51, 53, 57, 79, 85]

for n in numbers : 
    isprime = True
    div = -1
    
    for i in range(2, n):
        if n%i == 0 :
            isprime = False
            div = i
            break
    
    if isprime : print(f'{n}은(는) 소수입니다.')
    else : print(f'{n}은(는) 소수가 아닙니다. {div}은(는) {n}의 인수입니다.')       
```

