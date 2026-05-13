import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="오늘 날씨와 어울리는 노래",
    page_icon="🎵",
    layout="centered"
)

# 타이틀 및 날씨 소개
st.title("☀️ 오늘 날씨, 이 노래 어때요?")
st.markdown("### 현재 날씨: **맑음 (28°C / 북서풍 4 mph)**")
st.write("화창한 햇살과 기분 좋은 바람이 부는 오늘과 완벽하게 어울리는 선곡입니다. 🎧")

st.divider()

# 음악 추천 섹션 (유튜브 링크 및 가상 플레이어)
st.subheader("🌸 오늘의 추천 플레이리스트")

# 음악 1
with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.fontsize = 40
        st.markdown("# ☕")
    with col2:
        st.markdown("### **폴킴 - 모든 날, 모든 순간**")
        st.caption("장르: 발라드 | 추천 이유: 화창한 햇살 아래서 잔잔하게 듣기 가장 좋은 곡")
        st.video("https://www.youtube.com/watch?v=X1Z_Yt3nvlg") # 실제 유튜브 링크 예시

# 음악 2
with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("# 🍃")
    with col2:
        st.markdown("### **볼빨간사춘기 - 여행**")
        st.caption("장르: 인디/팝 | 추천 이유: 선선한 북서풍을 맞으며 드라이브할 때 청량함 폭발하는 곡")
        st.video("https://www.youtube.com/watch?v=xRb8hxwN5zc")

# 음악 3
with st.container(border=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("# ✨")
    with col2:
        st.markdown("### **Bruno Mars - 24K Magic**")
        st.caption("장르: 팝/펑크 | 추천 이유: 28°C의 활기찬 오후, 텐션을 기분 좋게 올려줄 신나는 리듬")
        st.video("https://www.youtube.com/watch?v=UqyT8IEBkvY")

st.divider()

# 사용자의 기분 선택에 따른 보너스 추천
st.subheader("💬 지금 내 기분은?")
mood = st.radio(
    "현재 기분에 맞는 버튼을 누르면 딱 맞는 한 줄 가사를 추천해 드려요.",
    ["설렘 가득한 기분", "여유롭고 나른한 기분", "퇴근/하교하고 싶은 기분"]
)

if mood == "설렘 가득한 기분":
    st.success("🎵 \"네가 없이 웃을 수 있을까...\" 오늘 같은 날 고백하기 딱 좋은 날씨네요!")
elif mood == "여유롭고 나른한 기분":
    st.info("🎵 \"저기 멀리 바다가 보여...\" 시원한 음료 한 잔 마시며 창밖을 바라보세요.")
else:
    st.warning("🎵 \"오늘 밤 바라본 저 달이 너무 처량해...\" 조금만 버티세요! 칼퇴를 기원합니다!")
