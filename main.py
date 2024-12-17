import streamlit as st

# 페이지 제목과 설명
st.title("🎭 나의 MBTI에 따른 직업 및 궁합 추천")
st.write("당신의 MBTI 유형을 선택하면, 어울리는 직업과 잘 맞는 사람 유형을 알려드릴게요! 😊")

# MBTI 유형 선택 드롭다운 메뉴
mbti_type = st.selectbox(
    "당신의 MBTI 유형을 선택하세요:",
    ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
     "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
)

# 각 MBTI 유형에 대한 정보
mbti_info = {
    "ISTJ": {
        "직업": "회계사, 관리자, 금융 분석가, 데이터 분석가, 법무사, 공무원, 엔지니어, 군인",
        "궁합": "ESFP, ESTP"
    },
    "ISFJ": {
        "직업": "간호사, 교사, 사회복지사, 상담사, 행정직, 약사",
        "궁합": "ESFP, ESTP"
    },
    "INFJ": {
        "직업": "심리학자, 작가, 상담사, 사회운동가, 종교 지도자, 예술가",
        "궁합": "ENFP, ENTP"
    },
    "INTJ": {
        "직업": "연구원, 과학자, 엔지니어, IT 전문가, 분석가, 교수",
        "궁합": "ENFP, ENTP"
    },
    "ISTP": {
        "직업": "엔지니어, 기술자, 파일럿, 소방관, 정비사",
        "궁합": "ESFJ, ESTJ"
    },
    "ISFP": {
        "직업": "예술가, 디자이너, 작가, 사진작가, 요리사",
        "궁합": "ESFJ, ESTJ"
    },
    "INFP": {
        "직업": "작가, 예술가, 상담사, 사회 운동가, 종교 지도자",
        "궁합": "ENFJ, ENTJ"
    },
    "INTP": {
        "직업": "연구원, 프로그래머, 수학자, 과학자, 엔지니어",
        "궁합": "ENTJ, ESTJ"
    },
    "ESTP": {
        "직업": "기업가, 경찰관, 운동선수, 세일즈 매니저, 홍보 전문가",
        "궁합": "ISFJ, ISTJ"
    },
    "ESFP": {
        "직업": "이벤트 플래너, 연예인, 퍼스널 트레이너, 교사, 상담사",
        "궁합": "ISFJ, ISTJ"
    },
    "ENFP": {
        "직업": "작가, 광고 기획자, 창업가, 상담사, 이벤트 기획자",
        "궁합": "INFJ, INTJ"
    },
    "ENTP": {
        "직업": "기업가, 마케팅 전문가, 변호사, 발명가, 연구원",
        "궁합": "INFJ, INTJ"
    },
    "ESTJ": {
        "직업": "관리자, 은행가, 공무원, 감독자, 법률가",
        "궁합": "ISFP, ISTP"
    },
    "ESFJ": {
        "직업": "교사, 간호사, 이벤트 플래너, 상담사, 사회복지사",
        "궁합": "ISFP, ISTP"
    },
    "ENFJ": {
        "직업": "심리학자, 교사, 사회복지사, 홍보 전문가, 리더십 코치",
        "궁합": "INFP, ISFP"
    },
    "ENTJ": {
        "직업": "CEO, 관리자, 전략 컨설턴트, 변호사, 기업가",
        "궁합": "INFP, INTP"
    }
}

# 사용자가 MBTI 유형을 선택했을 때 정보 표시
if mbti_type:
    st.subheader(f"당신의 MBTI 유형: {mbti_type}")
    st.write(f"**추천 직업:** {mbti_info[mbti_type]['직업']} 💼")
    st.write(f"**잘 맞는 사람 유형:** {mbti_info[mbti_type]['궁합']} 💖")
