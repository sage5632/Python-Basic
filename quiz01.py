def quiz1():

    str1 = "Life is too short, You need Python"
    # 알파벳 글자 수
    print("str1 length:", len(str1))

    # 글자를 모두 소문자
    print(str1.lower())

    #공백과 ,를 모두 제거
    print(str1.replace(" ","").replace(",",""))

    # 문자열을 list로 형변환후 lst 변수에 담기
    lst = str1.split()
    print(lst)

    # lst를 set으로 형변환 char 변수
    lst = set(lst)















# def quiz2():

if __name__ == "__main__":
    quiz1()
  #  quiz2()