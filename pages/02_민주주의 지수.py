import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="세계 경제 상위 10개국 민주주의 지수", layout="centered")

st.title("🌍 세계 경제 상위 10개국의 민주주의 지수")
st.markdown("2024년 GDP 기준 상위 10개국의 **민주주의 지수 (Democracy Index)** 비교")

# 데이터 생성
data = {
    "country": [
        "United States", "China", "Japan", "Germany", "India",
        "United Kingdom", "France", "Italy", "Brazil", "Canada"
    ],
    "gdp_rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "democracy_index": [7.85, 2.00, 8.15, 8.80, 6.71, 8.28, 7.99, 7.69, 6.86, 9.22]
}

df = pd.DataFrame(data)

# Plotly 시각화
fig = px.bar(
    df.sort_values("democracy_index", ascending=False),
    x="country",
    y="democracy_index",
    text="democracy_index",
    title="세계 경제 상위 10개국의 민주주의 지수",
    labels={"country": "국가", "democracy_index": "민주주의 지수"},
    color="democracy_index",
    color_continuous_scale="Blues"
)

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(yaxis=dict(range=[0, 10]), xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)
