import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

# 제목
st.title("🧬 생명공학에 대하여")
st.caption("작성자: C521044 윤대훈")

# 헤더
st.header("생명공학이란?")
st.write("""
생명공학(Biotechnology)은 생명체의 기능을 응용해 다양한 문제를 해결하는 과학 기술입니다.
유전자 편집, 인공 장기, 백신 개발, 식물 개량 등 다양한 분야에 사용됩니다.
""")

# 구분선
st.markdown("---")

# 이미지
st.subheader("DNA 구조")
st.image("https://cdn.ck12.org/media/02/09/02-09-06-10-dnarep.png", caption="DNA 복제 구조 (교육용)")

# 오디오
st.subheader("📢 유전자 편집 소개 오디오")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 비디오
st.subheader("🎥 유전자 가위 CRISPR 영상")
st.video("https://www.youtube.com/watch?v=2pp17E4E-O8")

# 수식
st.subheader("생명 에너지 공식")
st.latex(r"E = mc^2")
st.markdown("세포 내 에너지 전환은 생명 활동에 필수적인 과정입니다.")

# 데이터프레임
st.header("📊 생명공학 기술별 성장률 비교")
df = pd.DataFrame({
    '기술': ['CRISPR', '인공 장기', '백신 플랫폼', '세포 치료제'],
    '2022': [45, 60, 80, 55],
    '2025 예상': [75, 85, 90, 70]
})
st.dataframe(df)

# Altair 막대 차트
st.subheader("기술별 성장률 (Altair)")
alt_chart = alt.Chart(df).transform_fold(
    ['2022', '2025 예상'],
    as_=['연도', '성장률']
).mark_bar().encode(
    x='기술:N',
    y='성장률:Q',
    color='연도:N',
    column='연도:N'
).properties(title="2022년 vs 2025년 기술 성장률")
st.altair_chart(alt_chart, use_container_width=True)

# Altair 원형 차트 대체
st.subheader("2025년 예상 점유율 (Altair 원형 차트)")
alt_pie_df = df[['기술', '2025 예상']].rename(columns={'2025 예상': 'value'})
alt_pie = alt.Chart(alt_pie_df).mark_arc().encode(
    theta='value:Q',
    color='기술:N',
    tooltip=['기술', 'value']
).properties(title="2025년 기술별 점유율")
st.altair_chart(alt_pie, use_container_width=True)

# Matplotlib 그래프
st.subheader("ATP 생성 시뮬레이션 (Matplotlib)")
hours = np.arange(0, 24)
atp = np.sin(hours / 3) * 50 + 100

fig, ax = plt.subplots()
ax.plot(hours, atp)
ax.set_title("ATP 생성량 변화")
ax.set_xlabel("시간 (시)")
ax.set_ylabel("ATP 농도")
st.pyplot(fig)

# 코드 예시
st.subheader("🧬 DNA 염기 수 세기 예제 코드")
st.code("""
def count_bases(dna):
    return {
        "A": dna.count("A"),
        "T": dna.count("T"),
        "G": dna.count("G"),
        "C": dna.count("C")
    }

sample = "ATCGATTGAGCTCTAGCG"
count_bases(sample)
""", language='python')

# 코드 실행 예시
st.subheader("코드 실행 결과")
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

# 콜아웃 예시
st.subheader("💬 생명공학 기술 주의사항")
st.info("유전자 편집은 질병 치료에 획기적인 발전을 이끌 수 있습니다.")
st.success("백신 플랫폼은 팬데믹 대응에 큰 기여를 했습니다.")
st.warning("기술 남용은 윤리적 논란을 불러일으킬 수 있습니다.")
st.error("일부 기술은 아직 충분한 안전성 검증이 이루어지지 않았습니다.")

# 구분선
st.markdown("---")

st.markdown("📚 감사합니다! ")