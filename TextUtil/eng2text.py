#-*- coding:utf-8 -*-
from hangulize import hangulize

def eng2txt(text):
    # 영어와 비슷한 cym 사용
    return hangulize(text, 'cym')