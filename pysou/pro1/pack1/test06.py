'''
정규표현식
'''
import re

ss = '1234 abc가나다ABC_GOOD_555_6_만세_123_523'
print(re.findall(r'123', ss))    # r() : raw mode
print(re.findall(r'가나', ss))
print(re.findall(r'[0-5]', ss))
print(re.findall(r'[가-힣]', ss))
print(re.findall(r'[^가-힣]', ss))
print(re.findall(r'[0-5]+', ss))    # *, +, ?
print(re.findall(r'[0-5]{2}', ss))
print(re.findall(r'[0-5]{3}', ss))
print(re.findall(r'.23', ss))   # ., ^, $, |, ()