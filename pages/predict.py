import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

st.title("회원 이탈 여부 예측하기")

st.header("회원 정보를 입력하고 이탈 여부 예측하기")


selected = st.radio( '회원의 성별을 선택하세요' , ['남성','여성'] )
if selected == '남성':
    gender_value = 1
elif selected == '여성':
    gender_value = 0

selected = st.radio( '회원의 거주지 혹은 직장이 근처에 있나요?' , ['네','아니요'] )
if selected == '네':
    Near_Location_value = 1
elif selected == '아니요':
    Near_Location_value = 0

selected = st.radio( '회원이 제휴 기업의 직원인가요?' , ['네','아니요'] )
if selected == '네':
    Partner_value = 1
elif selected == '아니요':
    Partner_value = 0

selected = st.radio( '친구 추천 프로모션을 통해 가입한 회원인가요?' , ['네','아니요'] )
if selected == '네':
    Promo_friends_value = 1
elif selected == '아니요':
    Promo_friends_value = 0

selected = st.radio( '회원이 폰 번호를 제공 했나요?' , ['네','아니요'] )
if selected == '네':
    Phone_value = 1
elif selected == '아니요':
    Phone_value = 0

selected = st.radio( '계약기간이 얼마인가요?' , ['1개월','6개월','12개월'] )
if selected == '1개월':
    Contract_period_value = 1
elif selected == '6개월':
    Contract_period_value = 6
elif selected == '12개월':
    Contract_period_value = 12

selected = st.radio( '회원이 단체 수업에 참여하나요?' , ['네','아니요'] )
if selected == '네':
    Group_visits_value = 1
elif selected == '아니요':
    Group_visits_value = 0

Age_value = st.slider('회원의 나이가 어떻게 되나요?' , 0 , 100, 20)

Avg_additional_charges_total_value = st.number_input("총 추가 지출 비용은 얼마인가요?", min_value=0.0, format="%.15f")

Month_to_end_contract_value = st.slider('계약 종료까지 몇개월 남았나요?', 1, 12, 6)

Lifetime_value = st.number_input("회원의 총 이용 개월수는 얼마인가요?", min_value=0, format="%d")

Avg_class_frequency_total_value = st.number_input("전체 평균 수업 참여 빈도가 어떻게 되나요?(주 단위)", min_value=0.0, format="%.15f")

Avg_class_frequency_current_month_value = st.number_input("최근 한 달간 평균 수업 참여 빈도가 어떻게 되나요?(주 단위)", min_value=0.0, format="%.15f")


member_data = pd.DataFrame({
    'gender': gender_value,
    'Near_Location': Near_Location_value,
    'Partner': Partner_value,
    'Promo_friends': Promo_friends_value,
    'Phone': Phone_value,
    'Contract_period': Contract_period_value,
    'Group_visits': Group_visits_value,
    'Age': Age_value,
    'Avg_additional_charges_total': Avg_additional_charges_total_value,
    'Month_to_end_contract': Month_to_end_contract_value,
    'Lifetime': Lifetime_value, 
    'Avg_class_frequency_total': Avg_class_frequency_total_value,
    'Avg_class_frequency_current_month': Avg_class_frequency_current_month_value
}, index=[0])

model_list = ["결정트리", "서포트 벡터 머신"]

selected_model = st.selectbox("어떤 모델로 계산할까요?", model_list)

if selected_model == "결정트리":
    model_path = "../saved_model/best_dt.joblib"
elif selected_model == "서포트 벡터 머신":
    model_path = "../saved_model/best_svm.joblib"

loaded_model = load(model_path)
prediction = loaded_model.predict(member_data)

if st.button("예측 결과 확인하기"):
    st.write(f"예측된 결과: {'나갈 회원' if prediction[0] == 1 else '남을 회원'}")