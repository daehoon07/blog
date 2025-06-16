import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

# 블로그 제목
st.title("🧬 생명공학에 대하여")

# 작성자 정보
st.caption("작성자:C521044 윤대훈)

# 서론
st.header("생명공학이란?")
st.write("""
생명공학(Biotechnology)은 생명체의 기능을 응용하여 인류에 도움이 되는 제품과 기술을 개발하는 학문입니다.
대표적으로 유전자 편집, 백신 개발, 조직 재생, 바이오 연료 등이 포함됩니다.
""")

st.divider()

# 이미지 삽입 (DNA 이미지)
st.subheader("DNA 구조")
st.image("https://cdn.pixabay.com/photo/2016/03/31/19/14/dna-1295561_960_720.png", caption="DNA 이중 나선 구조")

# 오디오 설명
st.subheader("📢 유전자 편집 기술 (오디오 설명)")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 비디오 삽입 - CRISPR 기술 설명 영상
st.subheader("🎥 유전자 가위 CRISPR")
st.video("https://www.youtube.com/watch?v=2pp17E4E-O8")  # 실제 영상이 아니어도 예시로 사용 가능

st.divider()

# 수식 관련 설명
st.subheader("🔬 생명공학에서 에너지 계산")
st.latex(r"E = mc^2")

st.markdown("""
이 수식은 알버트 아인슈타인의 질량-에너지 등가 공식입니다.  
세포 수준에서도 에너지 전환은 중요한 생명 현상입니다.  
예: ATP 생성
""")

st.divider()

# 데이터프레임 - 생명공학 기술의 시장 성장
st.header("생명공학 기술별 시장 성장률")
df = pd.DataFrame({
    '기술': ['CRISPR', '인공 장기', '백신 플랫폼', '세포 치료제'],
    '2022': [45, 60, 80, 55],
    '2025 예상': [75, 85, 90, 70]
})
st.dataframe(df)

# Altair 차트
st.subheader("📊 기술별 성장 비교 (Altair)")
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

# Plotly 원형 차트
st.subheader("🧪 2025 예상 시장 비율 (Plotly)")
fig_pie = px.pie(df, values='2025 예상', names='기술', title='2025년 예상 시장 점유율')
st.plotly_chart(fig_pie)

# Matplotlib 그래프 - ATP 생성량 시뮬레이션
st.subheader("⚙️ ATP 생성량 시뮬레이션 (Matplotlib)")
hours = np.arange(0, 24)
atp = np.sin(hours / 3) * 50 + 100
fig, ax = plt.subplots()
ax.plot(hours, atp, label="ATP 생성량")
ax.set_xlabel("시간 (h)")
ax.set_ylabel("ATP (단위)")
ax.set_title("시간에 따른 ATP 생성량 변화")
st.pyplot(fig)

st.divider()

# 코드 블록 예시 - DNA 염기 수 세기
st.subheader("🧬 DNA 염기 수 세기 예제")
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

# echo()로 코드와 실행결과 동시에
st.subheader("🔍 DNA 분석 코드 실행 예시")
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
    st.write("염기 수:", result)

st.divider()

# Callout 콜아웃 박스
st.subheader("📌 생명공학 정보 콜아웃")
st.info("유전자 편집은 특정 유전자를 정밀하게 교정할 수 있는 기술입니다.")
st.success("코로나19 백신은 mRNA 기반 생명공학의 대표 사례입니다.")
st.warning("CRISPR 기술은 윤리적 문제도 함께 고려되어야 합니다.")
st.error("동물 실험 실패로 인해 임상시험이 지연되었습니다.")

# 마무리
st.markdown("""
---

이 블로그는 **저의 관심 분야인 생명공학에 대해 소개하는 블로그입니다**
""")