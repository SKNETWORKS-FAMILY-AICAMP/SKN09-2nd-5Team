import streamlit as st

st.title("lightGBM")

st.title("RandomForest 분석")
st.write("이 페이지에서는 RandomForest 모델 성능 분석을 보여줍니다.\n")

st.subheader('Confusion Matrix')
st.image("./image/lightgbm_confusion.png", caption="이미지 3", use_container_width=True)

st.subheader('Calibration Curve')
st.image("./image/light_gbm_Calibration.png", caption="이미지 2", use_container_width=True)

st.subheader('ROC Curve')
st.image("./image/lightGBM_ROC.png", caption="이미지 1",use_container_width=True)

# 설명 추가
st.markdown('''
### 결과 해석
1. **모델 성능 분석**:
- 혼동 행렬(Confusion Matrix)을 보면:
    - 진짜 음성(TN): 577건 (이탈하지 않을 것으로 예측했고 실제로 이탈하지 않음)
    - 거짓 양성(FP): 21건 (이탈할 것으로 예측했으나 실제로 이탈하지 않음)
    - 거짓 음성(FN): 37건 (이탈하지 않을 것으로 예측했으나 실제로 이탈함)
    - 진짜 양성(TP): 165건 (이탈할 것으로 예측했고 실제로 이탈함)

- 모델 성능 지표:
    - 정확도 93%: 전체 예측 중 약 93 정확함
    - 정밀도 94%: 이탈 예측 중 실제 이탈한 비율
    - F1 점수 95%: 정밀도와 재현율의 조화평균으로 양호한 수준
            
2. **Calibration Curve 분석**:
- 모델의 예측이 잘 보정(calibrated)되었음을 나타내며, 예측 확률이 높을수록 실제 양성 비율도 증가
- 그래프가 대각선(Perfectly Calibrated)에 가까울수록 모델의 예측이 신뢰할 수 있음을 의미
- 타 모델의 비해 상대적으로 예측한 확률이 실제 결과와 일관되지 않거나 변동이 크고 모델의 성능 지표와 확률 예측은 별개임을 확인
                       
3. **ROC 곡선 및 AUC 분석**:
- ROC 곡선은 모델이 양성과 음성을 잘 구분하고 있음. (곡선이 왼쪽 위 코너에 가까워질수록 모델의 성능이 우수함)
- AUC 값이 0.97으로 매우 높아, 모델이 92%의 확률로 양성과 음성을 구분할 수 있음을 보여줌.

#### **최종 결론**:
- 모델은 높은 정확도(93%), 정밀도(94%), F1 점수(95%)를 기록하며 우수한 성능을 보였지만, Calibration Curve에서 예측 확률과 실제 확률 간에 일관되지 않거나 변동성이 크다는 점이 나타남. 또한 AUC 값 0.97은 모델이 양성과 음성을 잘 구분. 이를 통해 모델의 성능은 우수하지만, 확률 예측에 대한 보정이 필요함을 알 수 있음.
''')


st.write("더 자세한 내용은 깃허브를 통해 확인하세요!")
st.markdown("[메인페이지로 가기](./app.py)")