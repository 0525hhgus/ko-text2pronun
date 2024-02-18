# ko-text2pronun
**외래어와 수사 변환**이 추가된 **한국어 텍스트 발음 변환 도구**
- 단위 의존 명사 및 화폐 통화 관련 수사 변환 로직

## How to use
```
>>> from TextUtil.process_text import process_txt
>>> InputText = "이 회사의 CEO는 project를 진행하면서 4개월 만에 934,500,000$의 수익을 올렸습니다."
>>> print(process_txt(InputText, True)) # 텍스트, 외래어 변환 여부
이 회사에 CEO는 프로젝트를 지냉아면서 사개월 마네 구만삼천사배고심만달러의 수이글 올렫씀니다.
```

## Reference
- [KoG2Padvanced: 파이썬 기반 한국어 발음 변환기](https://github.com/seongmin-mun/KoG2Padvanced)
```
@article{Munetal2022,
  author = {Mun, Seongmin and Kim, Su-Han and Ko, Eon-Suk},
  year = {2022},
  title = {A proposal to improve on existing Grapheme-to-Phoneme conversion models informed by linguistics},
  journal = {The Korean Society for Language and Information},
  volume = 26,
  number = {2},
  pages = {27--46}
}
```
- [Hangulize - 외래어 자동 한글 변환 모듈](https://github.com/sublee/hangulize)
