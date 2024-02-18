from G2P.KoG2Padvanced import KoG2Padvanced
from konlpy.tag import Kkma
from TextUtil.digit2text import digit2txt, NNGdigit2txt, CSign2txt
from TextUtil.eng2text import eng2txt
import re

def process_txt(text, engtrans = False):
    kkma = Kkma()

    result = ""
    pattern = re.compile(r'([가-힣]+)|([a-zA-Z.]+)|(\d[\d,.]*)|(\$|€|£|¥|￦)|(\s+)')

    matches = pattern.finditer(text)
    for match in matches:
        if match.group(1):  # Korean part
            result += KoG2Padvanced(match.group(1))
        elif match.group(2):  # English or special characters part
            if engtrans == True:
                if match.group(2)[1:].islower():
                    result += eng2txt(match.group(2))
                else:
                    result += match.group(2)
            else:
                result += match.group(2)
        elif match.group(3):  # Number part
            end_index = match.end(3)
            # NNG Case
            next_word = kkma.pos(text[end_index:])[0]
            if next_word[1] == "NNG" and next_word[0] not in ['달러', '유료', '파운드', '엔', '원']:
                result += KoG2Padvanced(NNGdigit2txt(match.group(3).replace(',', '')))
            else:
                result += KoG2Padvanced(digit2txt(match.group(3).replace(',', '')))
        elif match.group(4):  # Currency symbol part
            result += CSign2txt(match.group(4))
        elif match.group(5):  # Space part
            result += match.group(5)
    return result