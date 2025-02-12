import streamlit as st

st.title("Logistic Regression")

st.title("Logistic Regression 분석")
st.write("이 페이지에서는 Logistic Regression 모델 성능 분석을 보여줍니다.\n")

st.subheader('Confusion Matrix')
st.image("./image/lr_confusion_matrix.png", caption="이미지 3", use_container_width=True)

st.subheader('Calibration Curve')
st.image("./image/lr_Calibration_curve.png", caption="이미지 2", use_container_width=True)

st.subheader('ROC Curve')
st.image("./image/lr_roc_curve.png", caption="이미지 1",use_container_width=True)

# 설명 추가
st.markdown('''
### 결과 해석
1. **모델 성능 분석**:
- 혼동 행렬(Confusion Matrix)을 보면:
    - 진짜 음성(TN): 575건 (이탈하지 않을 것으로 예측했고 실제로 이탈하지 않음)
    - 거짓 양성(FP): 23건 (이탈할 것으로 예측했으나 실제로 이탈하지 않음)
    - 거짓 음성(FN): 44건 (이탈하지 않을 것으로 예측했으나 실제로 이탈함)
    - 진짜 양성(TP): 158건 (이탈할 것으로 예측했고 실제로 이탈함)

- 모델 성능 지표:
    - 정확도 91.50%: 전체 예측 중 약 92%가 정확함
    - 정밀도 86.81%: 이탈 예측 중 실제 이탈한 비율
    - F1 점수 82.29%: 정밀도와 재현율의 조화평균으로 양호한 수준
            
2. **Calibration Curve 분석**:
- 모델의 예측이 잘 보정(calibrated)되었음을 나타내며, 예측 확률이 높을수록 실제 양성 비율도 증가
- 그래프가 대각선(Perfectly Calibrated)에 가까울수록 모델의 예측이 신뢰할 수 있음을 의미
- 이 경우, 모델의 예측이 비교적 잘 보정되어 있지만, 예측 확률이 0.5 이하일 때와 0.9 이상일 때 실제 양성 비율이 다소 떨어지는 경향이 있다. 이는 특정 구간에서 모델의 신뢰도를 향상시킬 여지가 있음을 시사.            

3. **ROC 곡선 및 AUC 분석**:
- ROC 곡선은 모델이 양성과 음성을 잘 구분하고 있음. (곡선이 왼쪽 위 코너에 가까워질수록 모델의 성능이 우수함)
- AUC 값이 0.97으로 매우 높아, 모델이 97%의 확률로 양성과 음성을 구분할 수 있음을 보여줌. -> 모델의 분류 성능이 뛰어나며 신뢰할 수 있는 예측을 제공한다는 것을 의미.

#### **최종 결론**:
- 모델의 예측 성능이 전반적으로 우수하며, 특히 91.50%의 높은 정확도를 보임
- ROC 곡선과 AUC 분석 결과, 모델의 분류 성능이 매우 뛰어나며, 신뢰할 수 있는 예측을 제공함     

''')

st.write("더 자세한 내용은 깃허브를 통해 확인하세요!")