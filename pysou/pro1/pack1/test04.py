'''
집합형 자료형 : list - 순서 O, 수정 O, 중복 O (순서가 있기 때문에)
'''

a = [1,2,3]; b = [10, a, 20.5, True, '문자열']
print(a, id(a))
print(b, id(b))

print()

f = ['엄마', '아빠', '나', '여동생']
print(f, len(f), f[2])

f.append('남동생') # 가장 마지막에 추가
f.remove('나')   # 제거
f.insert(0, '할아버지') # 원하는 자리에 삽입 
f.extend(['삼촌', '조카'])  # 배열 추가 1
f += ['이모', '고모']   # 배열 추가 2
print(f)
print(f.index('남동생'))
print('엄마' in f, '나' in f)  # list 에 있는 자료 검색

print('\n슬라이싱')
aa = [1,2,3,4,5]
print(aa[0], ' ' , aa[0:3], ' ', aa[-1], aa[::2])    # 음수는 뒤에서 부터 / '::' : 증가치

aa = [1,2,3, ['a','b','c'], 4,5]
aa[0] = 100 # 수정 가능
print(aa)
aa[3][0] = 'good'   # 이중배열 호출
print(aa)
print(aa[0], aa[3])
print(aa[3], aa[:2])    # aa[:2] : a[2] 전까지

print()

print(aa)
aa.remove(4)    # 값에 의한 삭제
del aa[4]   # 순서(index)에 의한 삭제
print(aa)
aa[3].remove('c')
del aa[3][0]
print(aa)

print()

aa2= [3,1,5,2,4]
print(aa2)
aa2.sort()
print(aa2)
aa2.sort(reverse = True)
print(aa2)
aa3 = sorted(aa2)
print(aa2)
print(aa3)

print()

aa4 = ['123', '34', '234']  # 문자열
aa4.sort()
print(aa4)

aa4.sort(key=int)
print(aa4)

print('\n복사')
name = ['tom','james','oscar']
name2 = name    # 주소 치환 = 얕은 복사
print(name, name2, id(name), id(name2))
name[0] = 'john'
print(name, name2)

import copy
name3 = copy.deepcopy(name) # 새로운 주소를 가짐 = 깊은 복사
name[0] = 'page'
print(name, name3, id(name), id(name3))

print()
sbs = [10,20,30]
sbs.append(40)  # stack : LIFO
print(sbs)
sbs.pop()
sbs.pop()
print(sbs)

print()

sbs = [10,20,30]
sbs.append(40)  # queue : FIFO
print(sbs)
sbs.pop(0)
sbs.pop(0)
print(sbs)


















