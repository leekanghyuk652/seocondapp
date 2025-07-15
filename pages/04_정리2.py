import streamlit as st

st.set_page_config(page_title="GDP와 정치체제 비교", layout="wide")
st.title("🌍 GDP 상위국: 민주주의 국가 다수 vs 중국의 예외적 성장")

# 비교 표 출력
st.subheader("📊 비교 요약 표")

headers = ["항목", "민주주의 국가 (대다수)", "중국 (비민주 국가 예외)"]
rows = [
    ["정치 체제", "다원적, 선거 기반", "일당 체제, 중앙 통제"],
    ["정책 실행 방식", "참여적, 느리지만 합의 중심", "신속하지만 권위적"],
    ["법치와 권리", "표현의 자유, 사유 재산 보호", "제한된 권리, 통제 중심"],
    ["경제 모델", "민간 중심의 시장경제", "국가 주도 자본주의"],
    ["성장 방식", "혁신, 무역, 교육 기반", "계획경제, 인프라 주도"],
    ["장점", "제도적 안정성, 사회 신뢰", "정책 일관성, 빠른 집행"],
    ["리스크", "정책 지연 가능성", "표현 통제, 지속가능성 우려"],
]

# HTML 테이블 렌더링 (라이브러리 없이)
st.markdown(
    "<style>th, td {text-align: center !important; padding: 6px;}</style>", 
    unsafe_allow_html=True
)

html = "<table style='width:100%; border-collapse: collapse;' border='1'>"
html += "<thead style='background-color: #f0f2f6;'><tr>"
html += "".join(f"<th>{h}</th>" for h in headers)
html += "</tr></thead><tbody>"

for row in rows:
    html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"

html += "</tbody></table>"

st.markdown(html, unsafe_allow_html=True)

# 해석 부분
st.subheader("📝 분석 요약")

with st.expander("✅ 왜 민주주의 국가가 많은가?"):
    st.write("""
    - 정치적 투명성과 법치주의는 투자와 기업활동에 신뢰를 제공  
    - 표현의 자유 → 혁신과 교육 활성화  
    - 시장경제와 제도적 안정성 덕분에 지속적인 경제 성장 가능
    """)

with st.expander("✅ 중국이 강력한 이유는?"):
    st.write("""
    - 중앙정부 주도의 집중 투자, 계획경제  
    - 거대한 인구 기반과 세계 공급망 중심 국가  
    - 표현과 자유는 제한하지만, 빠른 정책 집행력으로 성장 견인
    """)

with st.expander("📌 결론"):
    st.write("""
    - 민주주의는 일반적으로 경제 번영에 유리  
    - 중국은 예외적으로 국가주도의 압축 성장 성공  
    - 향후 지속가능성과 사회 통제 문제는 중요한 변수
    """)

st.markdown("---")
st.caption("© 2025 정치체제와 경제력 비교 대시보드")
