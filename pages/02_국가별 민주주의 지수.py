import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 기본 설정
st.set_page_config(page_title="Democracy Index 지도 시각화", layout="wide")
st.title("🌍 세계 민주주의 지수 지도")
st.write("국가별 민주주의 점수를 Folium을 이용해 지도 위에 시각화한 웹앱입니다.")

# CSV 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("democracy_index_with_coords.csv")
    return df

df = load_data()

# 데이터 확인
with st.expander("📄 데이터 미리보기"):
    st.dataframe(df)

# 지도 생성
m = folium.Map(location=[20, 0], zoom_start=2)

# 컬럼명이 일치하는지 확인
if "Latitude" in df.columns and "Longitude" in df.columns and "Country" in df.columns and "Score" in df.columns:
    for _, row in df.iterrows():
        popup_html = f"""
        <b>{row['Country']}</b><br>
        민주주의 지수: {row['Score']}<br>
        분류: {row.get('Category', 'N/A')}
        """
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=6,
            color="green" if row["Score"] >= 8 else "orange" if row["Score"] >= 6 else "red",
            fill=True,
            fill_opacity=0.7,
            popup=folium.Popup(popup_html, max_width=250)
        ).add_to(m)
else:
    st.error("❌ 데이터에 'Latitude', 'Longitude', 'Country', 'Score' 컬럼이 포함되어야 합니다.")

# Folium 지도 출력
st_data = st_folium(m, width=1000, height=600)
