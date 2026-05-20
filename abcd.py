import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정 및 제목
st.set_page_config(page_title="용돈 기입장", page_icon="💰", layout="centered")
st.title("💰 오늘 나의 지출 기록기")
st.write("오늘 하루 동안 쓴 돈을 기록하고 소비 습관을 점검해봐!")

# 스트림릿에서 데이터를 임시로 저장하기 위한 바구니(세션 변수) 만들기
if "spending_list" not in st.session_state:
    st.session_state.spending_list = []

st.write("---")

# 2. 지출 입력 창 영역
st.subheader("✍️ 오늘 쓴 돈 입력하기")

# 가로로 깔끔하게 배치하기 위해 칸 나누기
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    category = st.selectbox("카테고리", ["식비 🍔", "교통비 🚌", "쇼핑 🛍️", "문화/취미 🎬", "기타 🎸"])
with col2:
    amount = st.number_input("금액 (원)", min_value=0, step=100, value=0)
with col3:
    st.write("") # 줄바꿈용 빈 칸
    st.write("") 
    add_button = st.button("추가하기")

# [추가하기] 버튼을 누르면 리스트에 저장
if add_button and amount > 0:
    st.session_state.spending_list.append({"카테고리": category, "금액(원)": amount})
    st.toast("지출 내역이 추가되었어! 🎉")

st.write("---")

# 3. 결과 출력 및 그래프 영역
st.subheader("📊 오늘의 소비 리포트")

if not st.session_state.spending_list:
    # 아직 아무것도 입력하지 않았을 때 (무지출 상태)
    st.info("🎉 아직 지출이 없어! 오늘의 무지출 챌린지 성공 중 👑")
else:
    # 입력된 데이터가 있을 때 표(DataFrame)로 만들기
    df = pd.DataFrame(st.session_state.spending_list)
    
    # 오늘 총 지출 계산
    total_amount = df["금액(원)"].sum()
    
    # 대시보드 형태로 총액 보여주기
    st.metric(label="💵 오늘 총 지출 금액", value=f"{total_amount:,} 원")
    
    # 칭찬 혹은 잔소리 코멘트
    if total_amount <= 10000:
        st.success("대단해! 오늘 소비를 아주 잘 아꼈어. 칭찬해! 👏")
    elif total_amount <= 30000:
        st.warning("적당하게 잘 썼네! 내일은 조금만 더 아껴볼까? 😉")
    else:
        st.error("앗, 오늘 지출이 조금 과한데? 지름신이 오셨나 봐요! 💸")
        
    # 데이터 표와 그래프 보여주기
    tab1, tab2 = st.tabs(["📝 상세 내역 보기", "📊 카테고리별 그래프"])
    
    with tab1:
        st.dataframe(df, use_container_width=True)
        # 내역 초기화 버튼
        if st.button("🗑️ 전체 내역 지우기"):
            st.session_state.spending_list = []
            st.rerun()
            
    with tab2:
        # 카테고리별로 묶어서 그래프 그리기
        chart_data = df.groupby("카테고리")["금액(원)"].sum()
        st.bar_chart(chart_data)
