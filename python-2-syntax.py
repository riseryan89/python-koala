
# 괄호가 없는 대신 들여쓰기가 문법
# 여러사람이 한 프로젝트를 다룰 때 포멧터를 사용함 (예, Black)
# https://black.readthedocs.io/en/stable/

a = 123

if a == 123:
    print("a 는 123 입니다.")

# PEP-8

# 탭이냐.. 공백이냐..
# 한 행의 길이 79자
# 쓸데없는 공백

a = []
b = a[ 2 ]
print ("Hello")

a = None

if a == None:
    print("a 는 None 입니다.")

if a is None:
    print("a 는 None 입니다.")


# Singleton 인 경우 is 로 체크
