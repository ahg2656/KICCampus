'''
tuple : list 와 유사, 읽기 전용(수정 X), list 보다 검색속도가 빠름
'''

# t = 'a', 'b', 'c', 'd'
t = ('a', 'b', 'c', 'd')
print(t, len(t), t.count('a'), t.index('b'))

print()

p = (1,2,3)
print(p)
# p[0] = 10    # err : 'tuple' object does not support item assignment
q = list(p)     # 형변환
q[0] = 10
p = tuple(q)
print(p)

print("\n값 교환")

t1 = 10, 20
a, b = t1
b, a = a, b
t2 = a, b
print(t2)

print('***' * 10)
'''
set : 순서 X, 중복 X
'''
a = {1,2,3,1}
print(a, ' ' , len(a))
# print(a[0]) # err : 'set' object does not support indexing
b = {3, 4}
print(a.union(b))   # 합집합
print(a.intersection(b))    # 교집합
print(a - b, a | b, a & b)  # 차집합 / 합집합 / 교집합
b.add(5)    # 추가 가능
b.update({5,6,7})   # set 추가
b.update([8,9])     # list 추가
b.update((10,11))   # tuple 추가
b.update((12,))     # b.update((12))    # err : tuple 은 요소가 하나일 경우 마지막에 , 추가해야함
print(b)

b.discard(7)    # 값에 의한 삭제 - 해당 값 없으면 통과
b.remove(8)     # 값에 의한 삭제 - 해당 값 없으면 정지
b.discard(7)
# b.remove(8)    # err
print(b)

print()


li = [1,2,3,1,4]
print(li)
s = set(li)     # 중복제거
li = list(s)
print(li)

print('***' * 10)
'''
dict(key : value) : 순서 X, json 데이터 처리 시 용이
'''
mydic = dict(k1=1, k2='abc', k3=5.6)
print(mydic)
dic = {'파이썬':'뱀','자바':'커피','스프링':'용수철'}
print(dic)
print(len(dic))
print(dic['자바'])    # key 에 의한 검색
print(dic.get('자바'))
# print(dic['커피'])    # err : value 에 의한 검색 X
# print(dic[0])    # err : 순서가 없기 때문에

dic['오라클'] = '예언자'
print(dic)
print('오라클' in dic)
del dic["오라클"]  # 삭제
print(dic)
print(dic.keys())   # return : list (중복X)
print(dic.values()) # return : list (중복O)
dic.clear() # 전부 삭제
print(dic)








