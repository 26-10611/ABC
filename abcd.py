import streamlit as str

# 1. 웹사이트 타이틀 및 소개
st.set_page_config(page_title="기분 맞춤 노래 추천", page_icon="🎵")
st.title("🎵 오늘 네 기분은 어때?")
st.write("지금 느끼는 기분을 알려주면, 딱 어울리는 노래를 추천해줄게.")

# 2. 사용자 기분 입력 받기 (선택 상자 방식)
feeling = st.selectbox(
    "지금 네 기분 상태를 골라봐!",
    ("신나고 들뜸", "우울하고 지침", "잔잔하고 차분함", "몽글몽글 사랑스러움", "화가 난다!")
)

# 3. 기분별 노래 데이터베이스 (간단한 예시)
songs = {
    "신나고 들뜸": [
        {"title": "Dynamite - BTS", "url": "https://www.youtube.com/results?search_query=BTS+Dynamite"},
        {"title": "Hype Boy - NewJeans", "url": "https://www.youtube.com/results?search_query=NewJeans+Hype+Boy"}
    ],
    "우울하고 지침": [
        {"title": "한숨 - 이하이", "url": "https://www.youtube.com/results?search_query=이하이+한숨"},
        {"title": "위로 - 김필", "url": "https://www.youtube.com/results?search_query=김필+위로"}
    ],
    "잔잔하고 차분함": [
        {"title": "밤편지 - 아이유", "url": "https://www.youtube.com/results?search_query=아이유+밤편지"},
        {"title": "비가 오는 날엔 - 비스트", "url": "https://www.youtube.com/results?search_query=비스트+비가+오는+날엔"}
    ],
    "몽글몽글 사랑스러움": [
        {"title": "주저하는 연인들을 위해 - 잔나비", "url": "https://www.youtube.com/results?search_query=잔나비+주저하는+연인들을+위해"},
        {"title": "Everytime - 첸X펀치", "url": "https://www.youtube.com/results?search_query=첸+펀치+Everytime"}
    ],
    "화가 난다!": [
        {"title": "그라데이션 - 10CM", "url": "https://www.youtube.com/results?search_query=10CM+그라데이션"},
        {"title": "치얼업 - 트와이스", "url": "https://www.youtube.com/results?search_query=트와이스+치얼업"}
    ]
}

# 4. 추천 버튼 및 결과 출력
if st.button("🎵 노래 추천받기"):
    st.write("---")
    st.subheader(f"✨ '{feeling}' 상태인 너에게 추천하는 노래!")
    
    # 해당 기분의 노래 목록 가져오기
    recommended_songs = songs[feeling]
    
    for song in recommended_songs:
        st.markdown(f"- **[{song['title']}]({song['url']})** (클릭하면 검색 결과로 이동!)")
