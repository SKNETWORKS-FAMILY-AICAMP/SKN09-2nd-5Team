import streamlit as st

st.title("우리 팀의 프로젝트")
st.header("팀명: 예시팀")
st.write("""
    프로젝트에 대한 간단한 설명을 여기에 추가하세요.
    예를 들어, 우리가 해결하고자 하는 문제, 목표 등.
""")

st.subheader("프로젝트 목표")
st.write("""
    - 문제 정의
    - 해결 방법
    - 프로젝트 결과
""")

st.write("더 자세한 내용은 페이지를 통해 확인하세요!")
st.markdown("[페이지 1로 가기](./pages/page1)")
