import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load
from sklearn.preprocessing import StandardScaler
import shap
import matplotlib.pyplot as plt

st.title("회원 이탈 여부 예측하기")

st.write("회원 정보를 입력하고 이탈 여부 예측하기")

# 모델 파일 경로 지정
MODEL_PATHS = {
    "XGBoost (추천 모델)": "./saved_model/XGBoost.joblib",
    "랜덤 포레스트": "./saved_model/random_forest.joblib",
    "lightGBM": "./saved_model/lightGBM.joblib",
    "K-최근접이웃": "./saved_model/knn_model.joblib",
    "결정트리": "./saved_model/best_dt.joblib",
    "로지스틱 회귀": "./saved_model/best_lr.joblib",
    "서포트 벡터 머신": "./saved_model/best_svm.joblib",
}


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

Avg_additional_charges_total_value = st.number_input("총 추가 지출 비용은 얼마인가요?", min_value=0.0, format="%.16f")

Month_to_end_contract_value = st.number_input('계약 종료까지 몇개월 남았나요?')

Lifetime_value = st.number_input("회원의 총 이용 개월수는 얼마인가요?", min_value=0, format="%d")

Avg_class_frequency_total_value = st.number_input("전체 평균 수업 참여 빈도가 어떻게 되나요?(주 단위)", min_value=0.0, format="%.16f")

Avg_class_frequency_current_month_value = st.number_input("최근 한 달간 평균 수업 참여 빈도가 어떻게 되나요?(주 단위)", min_value=0.0, format="%.16f")


member_data = pd.DataFrame({
    'gender': [gender_value],
    'Near_Location': [Near_Location_value],
    'Partner': [Partner_value],
    'Promo_friends': [Promo_friends_value],
    'Phone': [Phone_value],
    'Contract_period': [Contract_period_value],
    'Group_visits': [Group_visits_value],
    'Age': [Age_value],
    'Avg_additional_charges_total': [Avg_additional_charges_total_value],
    'Month_to_end_contract': [Month_to_end_contract_value],
    'Lifetime': [Lifetime_value], 
    'Avg_class_frequency_total': [Avg_class_frequency_total_value],
    'Avg_class_frequency_current_month': [Avg_class_frequency_current_month_value]
}, index=[0])



# 값이 제대로 들어가는지 테스트용 코드
# st.write("gender:", gender_value)
# st.write("Near_Location:", Near_Location_value)
# st.write("Partner:", Partner_value)
# st.write("Promo_friends:", Promo_friends_value)
# st.write("Phone:", Phone_value)
# st.write("Contract_period:", Contract_period_value)
# st.write("Group_visits:", Group_visits_value)
# st.write("Age:", Age_value)
# st.write("Avg_additional_charges_total:", Avg_additional_charges_total_value)
# st.write("Month_to_end_contract:", Month_to_end_contract_value)
# st.write("Lifetime:", Lifetime_value)
# st.write("Avg_class_frequency_total:", Avg_class_frequency_total_value)
# st.write("Avg_class_frequency_current_month:", Avg_class_frequency_current_month_value)
# st.write("데이터 타입 확인:", member_data.dtypes)


# 세션 스테이트에서 모델을 미리 로드 (최초 실행 시만 로드)
if "models" not in st.session_state:
    st.session_state.models = {}
    for model_name, model_path in MODEL_PATHS.items():
        st.session_state.models[model_name] = load(model_path)
    st.success("모델 로딩 완료!")

# 선택 박스로 모델 선택
selected_model_name = st.selectbox("어떤 모델로 계산할까요?", list(MODEL_PATHS.keys()))

# 선택한 모델 불러오기
loaded_model = st.session_state.models[selected_model_name]

# 스케일러
df = pd.read_csv('./data/gym_churn_us.csv')
columns = ['Avg_additional_charges_total', 'Month_to_end_contract', 'Lifetime', 'Avg_class_frequency_total', 'Avg_class_frequency_current_month']
scaler = StandardScaler()
X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

if selected_model_name == "XGBoost (추천 모델)":
    df[columns] =scaler.fit_transform(df[columns])
    member_data[columns] = scaler.transform(member_data[columns])
prediction = loaded_model.predict(member_data)

# 버튼 눌러서 출력
if st.button("예측 결과 확인하기"):
    # print(prediction)
    st.write(f"예측된 결과: {'나갈 회원' if prediction[0] == 1 else '남을 회원'}")

    if selected_model_name == "XGBoost (추천 모델)":
        # SHAP explainer 생성
        explainer = shap.Explainer(loaded_model)
        shap_values = explainer.shap_values(X_test)
        fig, ax = plt.subplots()
    
        # SHAP Summary Plot
        shap.summary_plot(shap_values, X_test, show=False)
        st.pyplot(fig)
    
        # SHAP 값 테이블 출력
        shap_values_df = pd.DataFrame(shap_values[0].flatten(), columns=['SHAP_value'], index=X_test.columns)
        st.write(shap_values_df)
