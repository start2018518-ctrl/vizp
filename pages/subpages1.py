import streamlit as st

# 메인페이지 설정
st.set_page_config(
    page_title='서브페이지1',
    page_icon='smile',
    layout='centered',
    initial_sidebar_state='expanded'
)

st.write['서브페이지']

# side bar 추가
st.sidebar.title('다양한 사이드바 위젯들')

st.sidebar.checkbox('외')
st.sidebar.checkbox('고')
st.sidebar.divider()
st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])
st.sidebar.slider('나이', 0, 100, (20, 50))
st.sidebar.selectbox('지역', ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])

