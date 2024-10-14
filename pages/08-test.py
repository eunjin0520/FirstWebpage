import pandas as pd
import streamlit as st

@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",  # openpyxl 엔진을 사용하여 Excel 파일 읽기
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    return df

# Streamlit UI 구성
df = get_data_from_excel()
st.write(df)  # 데이터프레임을 Streamlit으로 출력
