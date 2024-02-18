#-*- coding:utf-8 -*-
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chandong83&logNo=221144077279
# 위 코드에서 추가 수정

# 만 단위 자릿수
tenThousandPos = 4
# 억 단위 자릿수
hundredMillionPos = 9
txtDigit = ['', '십', '백', '천', '만', '억']
txtNumber = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
txtPoint = '쩜 '

def digit2txt(strNum):
    resultStr = ''
    digitCount = 0
    # print(strNum)
    #자릿수 카운트
    for ch in strNum:
        # ',' 무시
        if ch == ',':
            continue
        #소숫점 까지
        elif ch == '.':
            break
        digitCount = digitCount + 1


    digitCount = digitCount-1
    index = 0

    while True:
        notShowDigit = False
        ch = strNum[index]
        #print(str(index) + ' ' + ch + ' ' +str(digitCount))
        # ',' 무시
        if ch == ',':
            index = index + 1
            if index >= len(strNum):
                break;
            continue

        if ch == '.':
            # [수정] 0.13 처럼 1이하의 값에 대한 처리 추가
            if strNum[index - 1] == '0' and not resultStr:
                resultStr = '영'
            resultStr += txtPoint
        else:
            # 자릿수가 2자리이고 1이면 '일'은 표시 안함.
            # 단 '만' '억'에서는 표시 함
            # [수정] digitCount >= 1으로 설정하여 '십' 단위에서도 표시
            if(digitCount >= 1) and (digitCount != tenThousandPos) and  (digitCount != hundredMillionPos) and int(ch) == 1:
                resultStr = resultStr + ''
            elif int(ch) == 0:
                resultStr = resultStr + ''
                # 단 '만' '억'에서는 표시 함
                if (digitCount != tenThousandPos) and  (digitCount != hundredMillionPos):
                    notShowDigit = True
            else:
                resultStr = resultStr + txtNumber[int(ch)]


        # 1억 이상
        if digitCount > hundredMillionPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-hundredMillionPos]
        # 1만 이상
        elif digitCount > tenThousandPos:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount-tenThousandPos]
        else:
            if not notShowDigit:
                resultStr = resultStr + txtDigit[digitCount]

        if digitCount <= 0:
            digitCount = 0
        else:
            digitCount = digitCount - 1
        index = index + 1
        if index >= len(strNum):
            break;
    return resultStr


NATIVE_MAP_ONES = {
    # "하나": 1, "둘": 2, "셋": 3, "넷": 4, "다섯": 5,
    "한": 1, "두": 2, "세": 3, "넷": 4, "다섯": 5,
    "여섯": 6, "일곱": 7, "여덟": 8, "아홉": 9,
    # "한": 1, "두": 2, "세": 3, "석": 3, "서": 3, "네": 4, "넉": 4, "너": 4,
    # "닷": 5, "엿": 6
}

MAP_TENS = {
    "열": 10, "스물": 20, "서른": 30, "마흔": 40, "쉰": 50,
    "예순": 60, "일흔": 70, "여든": 80, "아흔": 90
}


def NNGdigit2txt(number):
    # 이 함수는 주어진 숫자를 한국어 발음으로 변환합니다.
    # 예: 25 -> "스물다섯", 91 -> "아흔하나"
    # 여기서는 십 단위와 기본 숫자의 조합만을 고려합니다.
    korean_number = ""
    number = int(number)

    if  number >= 100:
        korean_number = digit2txt(str(number))
    elif number < 10:
        for key, value in NATIVE_MAP_ONES.items():
            if value == number:
                return key
    else:
        tens = number // 10
        ones = number % 10

        for key, value in MAP_TENS.items():
            if value == tens * 10:
                korean_number += key

        for key, value in NATIVE_MAP_ONES.items():
            if value == ones:
                korean_number += key

    return korean_number

def CSign2txt(csign):
    currency_symbols = {
        "$": "달러",
        "€": "유로",
        "£": "파운드",
        "¥": "엔",
        "￦": "원"
    }

    return currency_symbols.get(csign, "")