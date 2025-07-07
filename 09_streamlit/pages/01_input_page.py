import streamlit as st

st.title('사용자 입력 받는 페이지')

col1, _, col2 = st.columns(3)

with col1:
    nickname = st.text_input('닉네임 입력')
    age =st.number_input('나이 입력', min_value=13, max_value=100)

    options = ['한국', '중국', '일본', '미국', '외계']
    national = st.selectbox('국적',options)

    r_options = ['맛집 탐방', '영화감상', '음악감상', '뜨개질']
    hobby = st.radio('취미', r_options)


    is_cheked = st.checkbox('개인정보 제공 동의')

with col2:
    if st.button("입력 완료"):
        st.write(f'이름이 뭐야? {nickname}')
        st.write(f'몇살이야? {age}')
        st.write(f'어디서 살아? {national}')
        st.write(f'취미가 머야? {hobby}')
        st.write(f'개인정보 제공에 동의해? {is_cheked}')