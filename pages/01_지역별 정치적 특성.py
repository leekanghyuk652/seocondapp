import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="세계 지도 데이터 시각화", layout="wide")

st.title("🌍 세계 번영 및 정치 데이터 시각화")
st.write("업로드된 데이터를 기반으로 Folium 지도를 생성하고 국가별 정보를 지도 위에 표시합니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("global_prosperity_with_coords.csv")
    return df

df = load_data()

# 데이터 미리보기
with st.expander("📄 데이터 미리보기"):
    st.dataframe(df)

# 지도 생성
m = folium.Map(location=[20, 0], zoom_start=2)

# 좌표 열이 있는 경우 표시 (위도/경도 또는 나라별 중심좌표 필요)
if "Latitude" in df.columns and "Longitude" in df.columns:
    for _, row in df.iterrows():
        popup_text = ""
        for col in df.columns:
            popup_text += f"<b>{col}</b>: {row[col]}<br>"
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=5,
            color="blue",
            fill=True,
            fill_opacity=0.7,
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(m)
else:
    st.warning("⚠️ 지도에 표시할 좌표(Latitude, Longitude) 정보가 없습니다. 데이터에 위도와 경도가 포함되어야 지도 시각화가 가능합니다.")

# 지도 출력
st_data = st_folium(m, width=1000, height=600)
