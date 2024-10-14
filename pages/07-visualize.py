import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import numpy as np  # pip install numpy

# Streamlit 대시보드 설정
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- EXCEL 파일 읽기 ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # 'hour' 열 추가
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ---- 사이드바 ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# 필터링된 데이터프레임 생성
df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

# 데이터프레임이 비어 있는지 확인
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()  # 앱 실행 중지

# ---- 메인 페이지 ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")

# 제품군별 판매량 [바 차트]
sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")

# Streamlit의 내장 바 차트 사용
st.subheader("Sales by Product Line")
st.bar_chart(sales_by_product_line)

# 시간별 판매량 [바 차트]
sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()

# Streamlit의 내장 바 차트 사용
st.subheader("Sales by Hour")
st.bar_chart(sales_by_hour)

# ---- 스타일 숨기기 ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
