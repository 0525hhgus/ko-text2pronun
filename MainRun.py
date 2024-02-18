from TextUtil.process_text import process_txt

InputText = "이 회사의 CEO는 project를 진행하면서 4개월 만에 934,500,000$의 수익을 올렸습니다."

print(process_txt(InputText, True)) # 텍스트, 외래어 변환 여부