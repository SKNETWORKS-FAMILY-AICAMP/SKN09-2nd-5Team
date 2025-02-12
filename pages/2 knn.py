import streamlit as st

st.title("k-최근접 이웃 알고리즘 분석")
st.write("이 페이지에서는 k-최근접 이웃 알고리즘 모델 성능 분석을 보여줍니다.\n")

st.subheader('Confusion Matrix')
st.image("./image/knn_confusion_matrix.png", caption="이미지 3", use_container_width=True)

st.subheader('Calibration Curve')
st.image("./image/knn calibration curve.png", caption="이미지 2", use_container_width=True)

st.subheader('ROC Curve')
st.image("./image/knn_receiver curve.png", caption="이미지 1",use_container_width=True)

# 설명 추가
st.markdown('''
### 결과 해석
1. **모델 성능 분석**:
- 혼동 행렬(Confusion Matrix)을 보면:
    - 진짜 음성(TN): 561건 (이탈하지 않을 것으로 예측했고 실제로 이탈하지 않음)
    - 거짓 양성(FP): 37건 (이탈할 것으로 예측했으나 실제로 이탈하지 않음)
    - 거짓 음성(FN): 60건 (이탈하지 않을 것으로 예측했으나 실제로 이탈함)
    - 진짜 양성(TP): 142건 (이탈할 것으로 예측했고 실제로 이탈함)

- 모델 성능 지표:
    - 정확도 88%: 전체 예측 중 약 88 정확함
    - 정밀도 90%: 이탈 예측 중 실제 이탈한 비율
    - F1 점수 92%: 정밀도와 재현율의 조화평균으로 양호한 수준
            
2. **Calibration Curve 분석**:
- 모델의 예측이 잘 보정(calibrated)되었음을 나타내며, 예측 확률이 높을수록 실제 양성 비율도 증가
- 그래프가 대각선(Perfectly Calibrated)에 가까울수록 모델의 예측이 신뢰할 수 있음을 의미
-  모델이 잘 보정되어 있으며, 예측 확률이 실제 확률과 거의 일치함.
                       
3. **ROC 곡선 및 AUC 분석**:
- ROC 곡선은 모델이 양성과 음성을 잘 구분하고 있음. (곡선이 왼쪽 위 코너에 가까워질수록 모델의 성능이 우수함)
- AUC 값이 0.92으로 매우 높아, 모델이 92%의 확률로 양성과 음성을 구분할 수 있음을 보여줌.

#### **최종 결론**:
- 모델은 높은 정확도(88%)와 뛰어난 F1 점수(92%)를 통해 높은 예측 성능을 보임, 보정된 예측 확률로 실제 결과와 잘 일치함. 또한, AUC 값 0.92는 모델이 양성과 음성을 잘 구분함
''')

st.write("더 자세한 내용은 깃허브를 통해 확인하세요!")
st.markdown("[메인페이지로 가기](./app.py)")