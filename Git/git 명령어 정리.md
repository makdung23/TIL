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

* git log

  : 지금까지 쌓아온 commit의 목록 확인

* git status 

  : modified 되었지만 add 되지 않은 사항들 확ㅇ인 가능



* git remote -v

  : 연결된 원격 저장소 확인하기

* git remote rm

  : 원격 연결 끊기

* git log --oneline

  : commit 로그 좀 더 간단하게 한 눈에 보기