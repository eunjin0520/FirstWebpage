import streamlit as st 
import pandas as pd
from datetime import datetime as dt
import datetime

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

st.subheader('나이')
# 숫자 입력
number = st.number_input(
    label='당신의 나이를 입력해 주세요.', #질문
    min_value=10,                #최소값
    max_value=100,               #최대값
    value=16,                    #기본값
    step=1                       #값이 증가, 감소하는 단위
)
st.write('선생님과 나이 차이는:  ', 20-number)


st.subheader('Secret')
# 파일 다운로드 버튼
# 샘플 데이터 생성
# Dataframe이란, pandas라이브러리에서 제공하는 2차원 데이터 구조(엑셀과 유사)
dataframe = pd.DataFrame({   
    'Food': ['salad','pasta','DDokbokKi','pizza'],
    'Place': ['School', 'HanRiver', 'Flower', 'Library'],
    'Activity':['movie','baking','bicycle','Picture']
})

# 다운로드 버튼 연결
st.download_button(
    label='선생님이 3-2와 하고 싶은것',
    data=dataframe.to_csv(),     # dataframe을 csv 형태로 변환
    file_name='wish list.csv',          
    mime='text/csv'              #데이터 유형
)
# 체크 박스
agree = st.checkbox('소원을 이루어줄 것을 약속 하십니까?')
if agree:
    st.write('동의 해주셔서 감사합니다 :100:')



st.subheader('혈액형')
# 라디오 선택 버튼
blood_type = st.radio(
    '당신의 혈액형은 무엇입니까?',
    ('A형', 'B형', 'O형', 'AB형', '선택지 없음'))

# 각 혈액형에 대한 설명
blood_type_descriptions = {
    'A형': '당신은 :blue[꼼꼼하고 신중한 성격]을 가지고 있네요.',
    'B형': '당신은 :green[자유롭고 개성적인 성격]을 가지고 있네요.',
    'O형': '당신은 :red[사교적이고 자신감 있는 성격]을 가지고 있네요.',
    'AB형': '당신은 :blue[독특하고 창의적인 성격]을 가지고 있네요.'
}

# 선택된 혈액형에 따라 설명 출력
if blood_type in blood_type_descriptions:
    st.write(blood_type_descriptions[blood_type])
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")


st.subheader('MBTI')
# 버튼 클릭
button = st.button('티니핑 MBTI 검사')
if button:
    # 하이퍼링크 연결
    st.markdown("[구글로 이동하기](https://smore.im/quiz/5xjJqtXtZ1?tm)") 

# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ', '선택지 없음'),
    index=16  # 기본값을 "선택지 없음"으로 설정
)

# 각 MBTI에 대한 설명
mbti_descriptions = {
    'ISTJ': '당신은 :blue[현실적이고 책임감이 강한 관리자] 이시네요.',
    'ISFJ': '당신은 :blue[배려심이 깊고 신뢰할 수 있는 수호자] 이시네요.',
    'INFJ': '당신은 :blue[직관적이고 비전을 중시하는 조언자] 이시네요.',
    'INTJ': '당신은 :blue[전략적 사고를 갖춘 독립적인 계획가] 이시네요.',
    'ISTP': '당신은 :blue[문제 해결에 능하고 분석적인 장인] 이시네요.',
    'ISFP': '당신은 :blue[예술적이고 감성적인 성향을 가진 모험가] 이시네요.',
    'INFP': '당신은 :blue[이상주의적이고 깊은 감정을 가진 중재자] 이시네요.',
    'INTP': '당신은 :blue[논리적이고 호기심 많은 사색가] 이시네요.',
    'ESTP': '당신은 :blue[즉흥적이고 사교적인 활동가] 이시네요.',
    'ESFP': '당신은 :blue[활발하고 열정적인 연예인] 이시네요.',
    'ENFP': '당신은 :blue[창의적이고 자유로운 영혼을 가진 활동가] 이시네요.',
    'ENTP': '당신은 :blue[논쟁을 즐기고 혁신적인 발명가] 이시네요.',
    'ESTJ': '당신은 :blue[실용적이고 목표 지향적인 리더] 이시네요.',
    'ESFJ': '당신은 :blue[사교적이고 사람을 돌보는 지원자] 이시네요.',
    'ENFJ': '당신은 :blue[따뜻하고 카리스마 넘치는 리더] 이시네요.',
    'ENTJ': '당신은 :blue[대담하고 결단력 있는 통솔자] 이시네요.'
}

# 선택된 MBTI에 따라 설명 출력
if mbti in mbti_descriptions:
    st.write(mbti_descriptions[mbti])
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")



st.subheader('방명록')
 # 텍스트 입력
title = st.text_input(
    label='선생님에게 하고 싶은 말이 있나요?', 
    placeholder='방명록을 남겨 주세요'
)
st.write(f'당신이 남긴 메세지: :violet[{title}]')

# 다중 선택 박스
st.subheader('여행지 추천') 
destinations = st.multiselect(
    '가보고 싶은 여행지를 선택해 주세요.',  # 질문
    ['파리', '뉴욕', '도쿄', '시드니', '로마'], # 선택 옵션
    ['파리', '도쿄'])                        # 기본 선택 옵션

# 사용자가 선택한 여행지를 출력
if destinations:
    st.write(f'당신이 가보고 싶은 여행지는: :blue[{", ".join(destinations)}] 입니다.')
else:
    st.write('아직 가보고 싶은 여행지를 선택하지 않으셨네요.')

# 선택한 여행지에 맞는 맞춤 메시지
if '파리' in destinations:
    st.write('파리는 예술과 패션의 도시로, 에펠탑을 꼭 방문해야 합니다!')
if '뉴욕' in destinations:
    st.write('뉴욕은 활기찬 도시로, 타임스퀘어와 센트럴 파크가 유명합니다.')
if '도쿄' in destinations:
    st.write('도쿄는 현대와 전통이 공존하는 도시로, 신주쿠와 아사쿠사에서 멋진 경험을 할 수 있습니다.')
if '시드니' in destinations:
    st.write('시드니는 아름다운 항구와 오페라 하우스로 유명합니다. 서핑도 잊지 마세요!')
if '로마' in destinations:
    st.write('로마는 역사와 문화가 풍부한 도시로, 콜로세움과 바티칸은 필수 방문지입니다.')

 
st.subheader('음악 볼륨 조절')

# 볼륨 조절 슬라이더
volume = st.slider(
    '볼륨을 조절하세요:',
    0, 100, 50)  # 최소값, 최대값, 초기값
st.write(f'현재 설정된 볼륨은 {volume}% 입니다.')

