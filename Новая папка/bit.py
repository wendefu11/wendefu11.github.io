from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message

os.environ["_BARD_API_KEY"] = "dwga68JOoEd2EywNVRGLZ80hKuUbk87cZ2UBNQ3EoaEuVypdX-J3DMSSlNAz8vjZ42kRIg."

message = 'Give the prices of bitcoin in a 7 days range as well as the explanation of the reasons for it to change. Make your answer based on the internet articles highlighting the main point.'
message2 = 'Give the prices of latoken in a 7 days range as well as the explanation of the reasons for it to change. Make your answer based on the internet articles highlighting the main point.'


st.title('Analyzer')

def response_api(promot):
    message=Bard().get_answer(str(promot))['content']
    return message

def responce_api_2(promot):
    message = Bard().get_answer(str(promot))['content']
    return message
    
on = st.toggle('Latocen')
if on:
   st.write(responce_api_2(message2))

if st.button("Bitok", type='primary'):
    st.write(response_api(message))
    
if 'generate' not in st.session_state:
    st.session_state['generate']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]

