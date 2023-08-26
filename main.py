# pip3 install python-dotenv 

## 환경설정을 불러오기 위한 라이브러리 
#from dotenv import load_dotenv

## 환경설정 불러오기 
#load_dotenv()


################################################################
######## Lang Chain ############################################
################################################################

# site : https://www.langchain.com/
# docs : https://python.langchain.com/docs/get_started/introduction.html

#pip3 install langchain
#pip3 install openai

# #### LLM Version ######
# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은")
# print(result)


# #### chat version #####
# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()

# ## 주제 
# content = "코딩"

# result = chat_model.predict(content + "에 대한 시를 써줘")
# print(result)

import langchain
#### chat version #####
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()


################################
####### Streamlit ##############
################################

import time
import streamlit as st

st.title('인공지능 시인 :blue[cool] :sunglasses:')

title = st.text_input('시의 주제를 제시해주세요', '')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중...'):
        result = chat_model.predict(title + "에 대한 시를 써줘")
        st.write(result)
    #st.success('Done!')    

### input 
st.write('시의 주제는', title)





