import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

st.title('게임 케릭터 인지도')

data = pd.DataFrame({
    '캐릭터':['전사', '법사', '힐러', '탱커', '랜덤'],
    '선택횟수':[120, 95, 150, 80, 111],
    '승률 (%)': [52, 48, 56, 60, 49],
    '인지도 (%)':[25, 20, 30, 15, 22]
})

st.dataframe(data)

st.bar_chart(data.set_index('캐릭터')['선택횟수'])
st.line_chart(data.set_index('캐릭터')['승률 (%)'])

fig = data.plot.pie(
    y='인지도 (%)',
    labels=data['캐릭터'],
    autopct='%1.1f%%',
    figsize=(6, 6),
    legend=False
).get_figure()
st.pyplot(fig)