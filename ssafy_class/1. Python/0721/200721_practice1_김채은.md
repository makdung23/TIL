<h1> 200721 practice1</h1> <h3>서울 4기 1반 김채은</h3>



<h5>1. 갯수 구하기</h5>

```python
students = ['김철수', '이영희', '조민지']
print(len(students))
```

<h5>2. 득표수 구하기</h5>

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
print(students.count("이영희"))
```

<h5>3. 최댓값 구하기</h5>

```python
numbers = [7, 10, 22, 4, 3, 17]
print(max(numbers))
```

<h5>4. 최솟값 구하기</h5>

``` python
numbers = [7, 10, 22, 4, 3, 17]
print(min(numbers))
```

<h5>5. 최댓값과 등장 횟수 구하기</h5>

```python
numbers = [7, 10, 22, 7, 22, 22]
print(max(numbers), numbers.count(max(numbers)))
```

<h5>6. 5의 개수 구하기</h5>

```python
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
print(numbers.count(5))
```

<h5>7.  'a'가 싫어</h5>

```python
word = input()
new_word = ''

for w in word :
    if w != "a" : new_word += w
print(new_word)
```

<h5>8. 단어 뒤집기</h5>

```python
word = input()
new_word = ''

for w in word : 
    new_word = w+new_word
print(new_word)
```

