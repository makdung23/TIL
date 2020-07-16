#  0716 리눅스, 깃 명령어



- 리눅스에서 ls -a 했을 때 나오는 . / .. 은 숨김폴더 

- python -V(대문자) -> bash 버전 확인



```python
import os

root_path = os.getcwd() # 현 위치 알려줘
file_path = os.path.join(root_path, 'dummy') # root_path 에 'dummy' 붙여줘!

os.chdir(file_path) #cd랑 똑같아. 이 경로로 들어갈래!
files = os.listdir(".") #ls랑 똑같애. 현 위치의 폴더/파일 목록 확인!

for f in files : 
    os.rename(f, f'SAMSUNG_{f}') # 파일 이름 변경. rename('기존이름', '바뀔 이름')
```





### git 설정

- 버전을 만들어주는 애

- | 1. 로컬 (워킹 디렉토리) | 2. 버전 명시하기 전 임시 저장(stagint area) | 3. 커밋 완료(staged) |
  | ----------------------- | ------------------------------------------- | -------------------- |
  | TIL python startcamp    |                                             |                      |

  * 1-> 2 : add 
    
* git add .
  
* 2-> 3: commit
  
  * git commit -m "넣고싶은 커밋 문구" 
  
  * commit 전에 나를 증명할 필요!
  
      git config --global user.email '내 이메일' 
    git config --global user.name '내 이름? 닉?' 
  
  * git log :  지금까지 쌓아온 커밋 로그 보기
  
  * git status : 지금 현 상태. 이거 modified 된 거 같은데? 도 알려줘
  
    

-> 얘네들을 이제 원격저장소인 github!에 올릴거야

* 내 로컬 -> 깃헙 리포지토리에 연결!

  * git remote add origin git@github.com:makdung23/TIL.git

    : 깃 프로그램아, 원격저장소를 추가해줘! origin이라는 이름으로!

* 이제 내 로컬 폴더/파일들을 -> 깃헙 리포지토리에 ** 추가! **
  
  * git push origin master 

