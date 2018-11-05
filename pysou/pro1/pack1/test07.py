'''
조건판단문 if
'''

var = 5

if var >= 3:
    print('크구나')
    print('참')  # Tab 을 기준으로 구분
else:
    print('거짓')
    
print('end1\n')    

jumsu = 80
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    print('저조') 
    
print('end2\n')

# jumsu = int(input('점수 입력 : '))  # int(), str()
if 90 <= jumsu <= 100:
    print('우수')
elif 70 <= jumsu <90:
    print('보통')
else:
    print('저조')

print('end3\n')

names = ['tom', 'james', 'oscar']
if 'oscar' in names:
    print('ok')
else:
    print('no')
print('end4\n')

a = 3
if a > 5:
    re = a * 2
else:
    re = a + 2
print(re)

re = a * 2 if a > 5 else a + 2  # 위와 같음
print(re)

a = 3
print((a + 2, a * 2)[a > 5])    # tuple 의 0번째 값




