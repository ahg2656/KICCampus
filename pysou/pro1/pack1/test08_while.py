'''
while
'''

a = 1
while a <= 5:
    print(a, end = ' ')
    a += 1

print()
colors = ['r','g','b']

print(colors[0])
a = 0
while a < len(colors):
    print(colors[a], end = ' ')
    a += 1

print()

while colors:
    print(colors.pop())
print(len(colors))

print()

a = 0
while a < 10:
    a += 1
    if a == 5: continue
    if a == 6: break
    print(a)
else:
    print('정상 종료 시 while 수헹')   # while 조건문 이외의 것에 의해 종료된 경우 출력 X

print('while 수행 후 : %d' %(a,))    

print()

while True:
    a = int(input("확인할 숫자 : "))
    if a == 0:
        print("종료")
        break
    elif a % 2 == 0:
        print("짝수")
        continue
    elif a % 2 == 1:
        print("홀수")
        continue
    
    
    
    
    
    
    