import streamlit as st
import matplotlib.pyplot as plt

# 예제 데이터
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 그래프 생성
plt.plot(x, y)

# Streamlit에서 그래프 출력
st.pyplot(plt)
