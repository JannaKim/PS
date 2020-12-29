#!/usr/bin/python
 
## 단어의 빈도수를 카운트 할 dictionary 를 만듭니다
word_dic = {}
 
## 텍스트 파일을 한 줄씩 읽어서
with open("curri.txt",'r+') as fr: # 기존 파일에 데이터 그대로 두고 그 위에 덮어씁니다
   for line in fr:
        print(line)
        ## 한 줄을 소문자로 만들고 공백으로 잘라서 for 문으로 하나씩 뽑습니다
        #strip() 함수: 주어진 문자열에서 양쪽 끝의 공백과 \n 기호를 삭제
        for word in line.lower().strip().split():
            if (word == 'timeit'):
                fr.write("changed")

 
## sorted 함수로 dictionary의 items() 메서드로 반환된 튜플을 정렬해 줍니다
word_list = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)

print(fr)
fr.close()
