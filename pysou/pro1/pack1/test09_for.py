'''
for
'''

# for i in [1,2,3,4,5]:    # list
# for i in (1,2,3,4,5):    # tuple
for i in {1,2,3,4,5}:       # set
    print(i, end=" ")
else:
    print('\nfor 수행')
    
print()

li = [1,2,3]
for i, d in enumerate(li):
    print(i, " ", d)
    
print()

soft = {'java':"웹용언어", "파이썬":"만능언어", "mysql":"db"}
for i in soft.items():
    # print(i)    # tuple 형식 출력
    print(i[0] + ' ' + i[1])

for k,v in soft.items():
    print(k + ' ' + v)

print()
     
for i in soft.keys():
    print(i, end=" ")
    
print()

for i in soft.values():
    print(i, end=" ")
    
print('\n')
print('^^^' * 10)

li1 = [3,4,5]
li2 = [0.5,1,2]
for a in li1:
    for b in li2:
        print(a + b, end=" ")

print()
    
datas = [a + b for a in li1 for b in li2]    
for d in datas:
    print(d, end=' ')
    
print("\n단어 수 출력")
import re 
ss = '''방북 후 야당의 공세에 이어 이번엔 미국 정부의 대북 사업 계획 보고 논란 때문이다. 
정부의 요청에 따라 특별수행원 자격으로 방북길에 올랐지만, 후푹풍이 이어지고 있는 상황이다.
4일 재계에 따르면 지난 9월 18~20일 평양에서 열린 ‘남북 정상회담’ 특별수행원 자격으로 방북한 주요 그룹 총수들이 연일 곤혼스러운 상황이 연출되고 있다. 
당시 방북길에는 이재용 삼성전자 부회장과 최태원 SK그룹 회장, 구광모 LG그룹 회장이 같이 했고, 현대차 그룹은 정의선 총괄 수석부회장을 대신해 김용환 부회장이 다녀왔다. 
또 최정우 포스코그룹 회장과 현정은 현대그룹 회장이 특별수행원 자격으로 방북했다.
하지만 총수들의 방북 이후 예기치 않은 곳에서 잇따라 불똥이 튀었다. 
처음으로 국회 농림축산식품해양수산위원회(농해수위) 소속 한국당 등 야당 의원들이 방북한 재계 총수들을 농림축산식품부 국정감사 증인으로 신청을 추진했다. 
여당인 더불어민주당의 반대로 총수 대신 전무급 간부를 소환하는 것으로 수위를 낮췄다.   
'''
ss2 = re.sub(r"[^가-힣\s]", '', ss)    # 한글과 공백을 제외한 나머지는 제거    
print(ss2)    
ss3 = ss2.split(' ')    # list type
print(ss3)
cou = {}    # 단어의 발생 횟수를 dict type 으로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1 # 같은 단어가 있으면 누적 
    else:
        cou[i] = 1
print(cou)
    
print()

for t_str in ['111-1234', '일이삼-사오육칠', '222-1234']:
    if re.match(r"\d{3}-\d{4}$", t_str):
        print(t_str, '전화번호 맞네')
    else:
        print(t_str, '이건 아니야')

print()

from time import localtime
print(localtime())
hour = localtime().tm_hour
print(hour)

act = {6:'잠', 9:'아침먹고 출근', 18:'일하기', 20:'야근', 24:'휴식'}
print(act)

for act_time in sorted(act.keys()):
    if hour < act_time:
        print(act[act_time])
        break
    
print('\n사전형 자료로 과일값 출력')
price = {'사과':2000, '감':500, '배':3000}
gogek = {'사과':3, '감':2}
bill = sum(price[f] * gogek[f] for f in gogek)
print("고객이 구입한 과일값은 {}원".format(bill))

print()

datas = [1,2,'a',True,3]
li = [i * i for i in datas if type(i) == int]
print(li)

datas = {1,1,2,2,2,3,1,1,1,1}
se = {i * i for i in datas}
print(se)

id_name = {1:'tom', 2:'james'}
name_id = {val:key for key, val in i
           d_name.items()}
print(name_id)

aa = [(1,2),(3,4),(5,6)]
print(aa)
for a, b in aa:
    print(a + b, end=" ")    
    
print()

print(list(range(1,6)))     # range() 를 이용해 수열값 얻기
print(set(range(1,6)))
print(tuple(range(1,6)))
print(list(range(-10,-50,-5)))
print(list(range(1,11,2)))

print()

# for i in range(1,6):    # 1 ~ 5
for i in range(6):      # 0 ~ 5
    print(i, end=' ')
    
print()
# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{}={} '.format(i,j,i*j), end = " ")
    print()

print()
# 주사위를 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(6):
    n1 = i + 1
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        if n % 4 == 0:
            print(n1, " ", n2)

for i in range(1,7):
    for j in range(1,7):
        if (i + j) % 4 == 0:
            print(i, " ", j)


print("\n----N-gram----")
ss = 'hello'
print(ss)
for i in range(len(ss) - 1):
    print(ss[i], ss[i+1], sep=' ')
    
print()
ss2 = 'this is python langu'
words = ss2.split()
print(words)
for i in range(len(words) - 1):
    print(words[i], words[i+1])    









    