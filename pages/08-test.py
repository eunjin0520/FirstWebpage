import streamlit as st
import plotly.express as px
import pandas as pd

# 샘플 데이터 생성
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [1, 4, 9, 16, 25]
})

# Plotly를 사용한 차트 생성
fig = px.line(data, x='x', y='y', title='Sample Plotly Line Chart')

# Streamlit에서 Plotly 차트 표시
st.plotly_chart(fig)
