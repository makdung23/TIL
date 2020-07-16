import os

root_path = os.getcwd() # 현 위치 알려줘
file_path = os.path.join(root_path, 'dummy') # root_path 에 'dummy' 붙여줘!

os.chdir(file_path) #cd랑 똑같아. 이 경로로 들어갈래!
files = os.listdir(".") #ls랑 똑같애. 현 위치의 폴더/파일 목록 확인!

for f in files : 
    os.rename(f, f'SAMSUNG_{f}') # 파일 이름 변경. rename('기존이름', '바뀔 이름')
# print(root_path)