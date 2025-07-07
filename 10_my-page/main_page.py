import streamlit as st

st.title('F1 퀄리파잉 및 레이싱 랩 타임 그래프로 보여주는 사이트')
st.subheader('퀄리파잉')

st.subheader('레이스')
my_site = st.text_input('오늘 내가 만들어보고 싶은 사이트는?!')
st.write(my_site)

if st.button(f'{my_site} 접속하기'):
    st.success(f'{my_site} 접속 중')