# -*- coding: utf-8 -*-
"""chatbot_using_gemenai.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FHW36eZaafRcPenIaGTuSqZsakmXuM5e
"""

!pip install google-generativeai

import google.generativeai as genai

genai.configure(
    api_key='your gemenai api key'
)

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

while(True):
  question=input("VIR:")
  if(question.strip()==''):
    break
  print('\n')
  response=chat.send_message(question)
  print(f"Vir: {response.text}")
  print('\n')

