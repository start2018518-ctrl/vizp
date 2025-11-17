import streamlit as st

st.title('111')

# 메인페이지 설정
st.set_page_config(
    page_title='streamlitprac',
    page_icon='🍉',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get help':'https://docs.streamlit.io',
        'Report a bug': 'https://streamlit.io'
    }
)

# side bar 추가
st.sidebar.title('다양한 사이드바 위젯들')

st.sidebar.checkbox('외국인 포함')
st.sidebar.checkbox('고령인구 포함')
st.sidebar.divider()
st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])
st.sidebar.slider('나이', 0, 100, (20, 50))
st.sidebar.selectbox('지역', ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])
