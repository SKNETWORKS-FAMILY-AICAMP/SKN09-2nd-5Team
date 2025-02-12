import streamlit as st
import numpy as np
import pandas as pd

st.title('결정트리(Decision Tree) 분석')
st.write("이 페이지에서는 결정트리(Decision Tree) 모델 성능 분석을 보여줍니다.")

st.subheader('Decision Tree 모델 시각화')
st.image('./image/DT_02.png', caption="Decision Tree 모델 시각화", use_container_width=True)

st.subheader("Confusion Matrix")
st.image('./image/DT_Confusion_Matrix.png', caption="Confusion Matrix", use_container_width=True)

st.subheader('Calibration Curve')
st.image('./image/DT_Calibration_Curve.png', caption="Calibration Curve", use_container_width=True)

st.subheader('ROC Curve')
st.image('./image/DT_ROC_after.png', caption="ROC Curve", use_container_width=True)


data = {
    '평가지표':['정확도(Accuracy)','정밀도(Precision)', '재현율(Recall)', 'F1-score', 'ROC-AUC'],
    '초기점수':[0.8762,0.7562,0.7525,0.7543,0.8353],
    '최적 하이퍼 파라미터 적용':[0.8812,0.8092,0.6931,0.7467,0.9064]
}
st.subheader("결정 트리 평가 지표 점수")
st.dataframe(data, hide_index=True)

# 설명 추가
st.markdown('''
### 결과 해석
1. **모델 성능 분석**:
- 혼동 행렬(Confusion Matrix)을 보면:
    - 진짜 음성(TN): 565건 (이탈하지 않을 것으로 예측했고 실제로 이탈하지 않음)
    - 거짓 양성(FP): 33건 (이탈할 것으로 예측했으나 실제로 이탈하지 않음)
    - 거짓 음성(FN): 62건 (이탈하지 않을 것으로 예측했으나 실제로 이탈함)
    - 진짜 양성(TP): 140건 (이탈할 것으로 예측했고 실제로 이탈함)

- 모델 성능 지표:
    - 정확도 88.12%: 전체 예측 중 약 88%가 정확함
    - 정밀도 80.92%: 이탈 예측 중 실제 이탈한 비율
    - F1 점수 74.67%: 정밀도와 재현율의 조화평균으로 양호한 수준
            
2. **Calibration Curve 분석**:
- 모델의 예측이 잘 보정(calibrated)되었음을 나타내며, 예측 확률이 높을수록 실제 양성 비율도 증가
- 그래프가 대각선(Perfectly Calibrated)에 가까울수록 모델의 예측이 신뢰할 수 있음을 의미
- 이 경우, 모델의 예측이 비교적 잘 보정되어 있지만, 낮은 확률(0~0.2) 구간에서 약간의 차이가 존재            

3. **ROC 곡선 및 AUC 분석**:
- ROC 곡선은 모델이 양성과 음성을 잘 구분하고 있음. (곡선이 왼쪽 위 코너에 가까워질수록 모델의 성능이 우수함)
- AUC 값이 0.90으로 비교적 높은 수치를 가지고 있어, 90% 가량의 신뢰할 수 있는 예측을 제공함

#### **최종 결론**:
- 모델의 예측 성능이 전반적으로 양호하며, 88.12%의 양호한 정확도를 보임
- ROC 곡선과 AUC 분석 결과, 모델의 분류 성능이 뛰어나며, 90% 가량의 신뢰할 수 있는 예측을 제공함     

''')

st.write("더 자세한 내용은 깃허브를 통해 확인하세요!")
