import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

# 제목
st.title("🧬 생명공학에 대해")

# 작성자 정보
st.caption("작성자: C521044 윤대훈")

# 헤더
st.header("생명공학이란?")
st.write("""
생명공학(Biotechnology)은 생물학의 원리를 응용하여 인류의 삶을 개선하는 기술입니다.
주요 예시로는 유전자 편집, 백신, 인공 장기 등이 있습니다.
""")

st.markdown("---")

# 이미지
st.subheader("DNA 구조")
st.image("https://cdn.pixabay.com/photo/2016/03/31/19/14/dna-1295561_960_720.png", caption="DNA 이중 나선")

# 오디오
st.subheader("📢 유전자 편집 기술 소개 (오디오)")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 비디오
st.subheader("🎥 유전자 가위 CRISPR 소개")
st.video("https://www.youtube.com/watch?v=2pp17E4E-O8")

st.markdown("---")

# 수식
st.subheader("E = mc^2 공식")
st.latex(r"E = mc^2")

st.markdown("세포 내 에너지 전환은 생명 활동에 필수입니다.")

# 데이터프레임
st.header("📊 생명공학 기술별 성장률")
df = pd.DataFrame({
    '기술': ['CRISPR', '인공 장기', '백신 플랫폼', '세포 치료제'],
    '2022': [45, 60, 80, 55],
    '2025 예상': [75, 85, 90, 70]
})
st.dataframe(df)

# Altair 차트
st.subheader("Altair 차트")
alt_chart = alt.Chart(df).transform_fold(
    ['2022', '2025 예상'],
    as_=['연도', '성장률']
).mark_bar().encode(
    x='기술:N',
    y='성장률:Q',
    color='연도:N',
    column='연도:N'
)
st.altair_chart(alt_chart, use_container_width=True)

# Plotly 차트
st.subheader("Plotly 원형 차트")
fig_pie = px.pie(df, values='2025 예상', names='기술', title='2025년 예상 시장 점유율')
st.plotly_chart(fig_pie)

# Matplotlib
st.subheader("ATP 생성 시뮬레이션")
hours = np.arange(0, 24)
atp = np.sin(hours / 3) * 50 + 100
fig, ax = plt.subplots()
ax.plot(hours, atp)
ax.set_title("ATP 생성량 변화")
ax.set_xlabel("시간 (시)")
ax.set_ylabel("ATP")
st.pyplot(fig)

st.markdown("---")

# 코드 블럭
st.subheader("🧬 DNA 염기 수 세기")
code = """
def count_bases(dna):
    return {
        "A": dna.count("A"),
        "T": dna.count("T"),
        "G": dna.count("G"),
        "C": dna.count("C")
    }

sample = "ATCGATTGAGCTCTAGCG"
count_bases(sample)
"""
st.code(code, language='python')

# echo() 코드 실행
st.subheader("코드 실행 예시")
with st.echo():
    def count_bases(dna):
        return {
            "A": dna.count("A"),
            "T": dna.count("T"),
            "G": dna.count("G"),
            "C": dna.count("C")
        }

    sample = "ATCGATTGAGCTCTAGCG"
    result = count_bases(sample)
    st.write("염기 수 결과:", result)

# 콜아웃
st.subheader("💡 생명공학 정보")
st.info("유전자 편집 기술은 질병 치료에 혁신을 가져올 수 있습니다.")
st.success("세포 치료제는 많은 환자에게 희망이 됩니다.")
st.warning("생명공학 기술은 윤리적 문제도 함께 고려해야 합니다.")
st.error("일부 기술은 안전성 검증이 부족합니다.")

# 구분선
st.markdown("---")
