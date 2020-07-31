# git 명령어 정리

### git 설정 시

- git config --global user.email '깃헙 가입한 이메일'

  git config --global user.name '내 이름/닉네임'

  : 내가 깃헙 사용자 누구임을 증명하는 것 

- git remote add origin *repository  주소*

  : git 프로그램에게 'origin'이라는 이름으로 repository주소에 대한 remote(원격) 저장소를 추가해달라고 요청



### commit, push  관련

- git add .

  : 로컬에서의 수정사항들을 staging area(임시저장소)에 옮겨 놓음 

- git add *helloworld.py*

  : 객체 하나만 add할 때

- git commit -m "커밋 설명 내용"

  : 지금까지 add되어 staging area에 머물러 있는 내용을 commit함. 일종의 labeling  

- git push origin master 

  :  지금까지 commit 내용들을 github repository(origin) 추가



* git remote -v

  : 연결된 원격 저장소 확인하기

* git remote rm

  : 원격 연결 끊기

* git log --oneline

  : commit 로그 좀 더 간단하게 한 눈에 보기



### Add / Commit 지우기

* add 취소

  git restore(버전에 따라 reset) --staged <add된 파일명>

* commit 수정 (**웬만하면 안하는게 !! **)

  * commit 메세지 수정

    git commit --amend -> 나오는 창에서 수정

  * 마지막 commit에 추가적인 파일 함께 commit

    git commit --amend 

    : 마지막 커밋 메세지 수정하며 지금 add 된 파일까지 함께 commit



###  기록 확인하기

* git log

  : 지금까지 쌓아온 commit의 목록 확인

* git status 

  : modified 되었지만 add 되지 않은 사항들 확ㅇ인 가능

* git diff

  : 어떤 파일에서 무엇이 삭제/추가되었는지 확인 가능

    **워킹스테이지**에 있는 수정사항들(add 하기 전)을 확인하는 것