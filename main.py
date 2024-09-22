import streamlit as st

# 타이틀 적용 예시
st.title("JINNY's Homepage:princess::heartbeat:")
st.header('Profile')

st.subheader('경력')
st.text('2023 ~ : 동대문중학교')
st.text('2020 ~ : 0000고등학교')

st.subheader('학력')
st.text('2000 ~ : 00중학교')
st.text('2004 ~ : 00고등학교')
st.text('2004 ~ : 00대학교')
st.caption('선생님 나이는 비밀이다.')

st.subheader('Contents')
st.markdown('Youtube: **지니제니** :red[★구독,댓글,좋아요 필수!!]')
st.markdown('Blog: *지니의 블로그*')
st.markdown('Instagram: **zinnyv.0.v** :red[맞팔해요~]')


st.subheader('좌우명')
sample_code = '''
def DoMyBest():
    print('Life is too short. You need python')
'''
st.code(sample_code, language="python")
 
 
