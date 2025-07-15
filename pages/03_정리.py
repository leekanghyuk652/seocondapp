import streamlit as st

st.set_page_config(page_title="선진국 vs 개발도상국 지표 비교", layout="wide")

st.title("🌍 선진국 vs 개발도상국: 주요 지표 비교 분석")

# 표 데이터 정의
headers = ["지표", "선진국 (평균 순위)", "개발도상국 (평균 순위)", "차이 설명"]
data = [
    ["average_score", "55.88", "110.27", "전반적인 번영 수준에서 선진국이 두 배 가까이 우수"],
    ["personal_freedom", "44.94", "123.86", "개인 자유도에서 큰 차이"],
    ["governance", "50.56", "116.89", "거버넌스 성과에서 선진국이 우세"],
    ["economic_quality", "60.34", "104.54", "경제 품질에서 선진국 우세"],
    ["living_conditions", "57.70", "107.02", "생활 수준 격차 큼"],
    ["education", "57.94", "106.64", "교육 분야 격차 큼"],
    ["health", "60.92", "104.42", "보건 성과에서도 선진국이 우세"],
]

# 표 출력
st.subheader("📊 지표별 평균 순위 비교")
st.markdown(
    "<style>th, td {text-align: center !important;}</style>", unsafe_allow_html=True
)
table_html = f"""
<table style='width:100%; border-collapse: collapse;' border='1'>
    <thead style='background-color: #f0f2f6;'>
        <tr>
            {''.join(f"<th>{h}</th>" for h in headers)}
        </tr>
    </thead>
    <tbody>
"""
for row in data:
    table_html += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
table_html += "</tbody></table>"

st.markdown(table_html, unsafe_allow_html=True)

# 해석 출력
st.subheader("📝 요약 해석")

with st.expander("전반적인 분석"):
    st.write("""
    - 전체 평균 점수(average_score)에서 선진국이 약 두 배 가까이 우수한 성과를 보임
    - 모든 지표에서 선진국이 개발도상국보다 더 나은 평균 순위를 기록
    """)

with st.expander("지표별 분석 요약"):
    st.markdown("""
    - **Personal Freedom**: 개인 자유도에서 약 79점 차이로 가장 큰 격차 발생  
    - **Governance**: 법치주의 및 정부 성과에서 약 66점 차이  
    - **Health**: 보건 성과 격차도 큼 (약 44점 차이)  
    - **Living Conditions / Education / Economic Quality**: 40~50점 사이의 격차로 전반적 생활 및 경제적 기반에서 큰 차이
    """)

with st.expander("종합 정리"):
    st.markdown("""
    - 개발도상국은 전 분야에서 구조적인 개선이 필요  
    - 개인 자유 및 거버넌스는 정치적·제도적 개혁이 핵심  
    - 선진국은 교육 및 건강 투자 → 경제적 성과로 이어짐  
    """)

st.markdown("---")
st.caption("© 2025 데이터 기반 국제 지표 비교 대시보드")



