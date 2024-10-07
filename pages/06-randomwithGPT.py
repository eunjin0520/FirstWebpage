# random_travel_recommender.py

import streamlit as st
import random

# 여행지 데이터를 리스트로 설정 (여기서는 간단히 몇 개의 여행지만 예시로 사용)
travel_destinations = {
    "Nature": ["Banff National Park, Canada", "Grand Canyon, USA", "Plitvice Lakes, Croatia", "Jeju Island, South Korea"],
    "City": ["New York, USA", "Tokyo, Japan", "Paris, France", "London, UK", "Seoul, South Korea"],
    "History": ["Rome, Italy", "Cairo, Egypt", "Athens, Greece", "Kyoto, Japan", "Machu Picchu, Peru"],
    "Adventure": ["Queenstown, New Zealand", "Patagonia, Argentina", "Iceland", "Norway Fjords", "Rocky Mountains, USA"]
}

# Streamlit 앱 타이틀
st.title("🌍 랜덤 여행지 추천기 🌍")

# 사용자에게 테마 선택 옵션 제공
st.subheader("여행 테마를 선택하세요:")
theme = st.selectbox(
    "어떤 테마로 여행을 떠나고 싶나요?",
    ("Nature", "City", "History", "Adventure")
)

# 랜덤 여행지 추천 버튼
if st.button('여행지를 추천해 주세요!'):
    destination = random.choice(travel_destinations[theme])
    st.subheader(f"추천하는 여행지는: :green[{destination}]")

    # 여행지에 대한 추가 설명을 제공할 수 있는 섹션
    st.write(f"{destination}는 {theme} 테마에 속하는 멋진 여행지입니다. 이곳을 방문하면 특별한 경험을 할 수 있습니다!")
