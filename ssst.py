import streamlit as st

# 메인페이지 설정
st.set_page_config(
    page_title='케데헌',
    page_icon='🍉',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get help':'https://docs.streamlit.io',
        'Report a bug': 'https://streamlit.io'
    }
)


st.title('케데헌 분석')
st.header('C321005 강찬영')



st.divider()



'# :orange[네트워크 시각화]'
# --------------------- llm 일부 사용 -> width=900 추가 -------------------------------
st.image("output1.png", width=900)
# -------------------------------------------------------------------------------


# --------------------- llm 일부 사용 -> "rb" 추가 -------------------------------
with open("output1.png", "rb") as file:
    st.download_button(
        label='그래프 다운로드',
        data=file,
        file_name='netv.png',
        mime='image/png'
    )
# -------------------------------------------------------------------------------


st.divider()

'# :orange[워드클라우드]'

st.image("output2.png", width=900)

with open("output2.png", "rb") as file:
    st.download_button(
        label='그래프 다운로드',
        data=file,
        file_name='wcv.png',
        mime='image/png'
    )








import pandas as pd
from itertools import combinations
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re
from konlpy.tag import Okt

df = pd.read_csv('kdh.csv')

descriptions = df['description'].tolist()

okt = Okt()

with open('korean_stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = f.read().splitlines()
    
all_nouns = []
for i, text in enumerate(descriptions):
    text_cleaned = re.sub(r'[^가-힣\s]', '', text)
    nouns = okt.nouns(text_cleaned)
    nouns = [word for word in set(nouns) if (len(word) > 1) and (word not in stopwords)]
    all_nouns.append(nouns)
    


# ---------------------------- llm 그대로 인용 ----------------------------------------------------------------
all_noun = [word for sublist in all_nouns for word in sublist]

# 2. 단어 출현 횟수 세기
counter = Counter(all_noun)

# 3. 데이터프레임으로 변환
df = pd.DataFrame(counter.items(), columns=["단어", "빈도"]).sort_values(by="빈도", ascending=False)

# -------------------------------------------------------------------------------------------------------

df = df.reset_index(drop=True).head(10)

st.divider()
'### :orange[Altair: 단어개수 top 15]'
import altair as alt
import pandas as pd
import numpy as np

c = (
    alt.Chart(df).mark_bar().encode(
        x='단어', y='빈도'
    )
)

st.altair_chart(c, use_container_width=True)





edge_list = []

for nouns in all_nouns:
    if len(nouns) > 1:
        edge_list.extend(combinations(sorted(nouns), 2))
        
edge_count = Counter(edge_list)

min_count = 20
filtered_edge = {edge: weight for edge, weight in edge_count.items() if weight >= min_count}

df2 = pd.DataFrame(filtered_edge.items(), columns=["edge", "빈도"]).sort_values(by="빈도", ascending=False).head(15)

# ----------------------- llm 그대로 인용------------------------
df2["edge_str"] = df2["edge"].apply(lambda t: "-".join(t))
# ---------------------------------------------------------------


'### :orange[Plotly: 네트워크 엣지 top 15]'
import plotly.express as px

fig = px.bar(df2, x="edge_str", y="빈도")

st.plotly_chart(fig)








all_adjectives = []
for i, text in enumerate(descriptions):
    text_cleaned = re.sub(r'[^가-힣\s]', '', text)
    
    #------------------llm 그대로 인용 ---------------------------------------------
    pos_result = okt.pos(text_cleaned)

    adjectives = [word for word, tag in pos_result if tag == "Adjective"]
    # ----------------------------------------------------------------------------------
    
    adjectives = [word for word in set(adjectives) if (len(word) > 1) and (word not in stopwords)]
    all_adjectives.append(adjectives)



all_adjective = [word for sublist in all_adjectives for word in sublist]

counter = Counter(all_adjective)

df3 = pd.DataFrame(counter.items(), columns=["단어", "빈도"]).sort_values(by="빈도", ascending=False).head(10)



'### :orange[seaborn: 등장 형용사 top 10]'
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt



fig, ax = plt.subplots()
sns.barplot(data=df3, x="단어", y="빈도", ax=ax)

st.pyplot(fig)


