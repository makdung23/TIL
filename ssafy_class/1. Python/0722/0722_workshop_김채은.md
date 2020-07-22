# 0722 Workshop

### 서울 4기 1반 김채은

<h5>1. List의 합 구하기</h5>

```python
def list_sum(listToSum) :
    result = 0
    for x in listToSum:
        result += x
    return result

print(list_sum([1,2,3,4,5]))
```

<h5>

<h5> 2. Dictionary로 이루어진 List의 합 구하기</h5>

```python
def dict_list_sum(listToSum):
    result = 0
    for d in listToSum :
        result += d['age']
    return result

print(dict_list_sum([{'name': 'kim', 'age': 12},
                     {'name': 'lee', 'age': 4}]))
```



<h5>3. 2차원 List의 전체 합 구하기</h5>

```python
def all_list_sum(listToSum):
    result = 0
    for inList in listToSum:
        for x in inList : 
            result += x
    return result

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
```





