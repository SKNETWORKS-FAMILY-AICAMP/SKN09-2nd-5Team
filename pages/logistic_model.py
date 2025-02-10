{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "왜 차이를 뒀는가? . / ..\n",
    ". (현재 디렉터리)\n",
    ".. (상위 디렉터리)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title(\"Model: Logistic Regression\")\n",
    "st.write(\"\"\"\n",
    "    결과 값 정리\n",
    "    1. confusion Matrix\n",
    "    2. Calibation Curve\n",
    "    3. ROC\n",
    "\"\"\")  \n",
    "\n",
    "\n",
    "\n",
    "st.line_chart([1, 2, 3, 4, 5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "\n",
    "st.title(\"Logistic Regression 분석\")\n",
    "st.write(\"이 페이지에서는 Logistic Regression  모델 성능 분석을 보여줍니다.\\n\")\n",
    "\n",
    "st.subheader('Confusion Matrix')\n",
    "st.image(\"./image/RF_Confusion Matrix.png\", caption=\"Confusion Matrix\", use_column_width=True)\n",
    "\n",
    "st.subheader('Calibration Curve')\n",
    "st.image(\"./image/RF_Calibration Curve.png\", caption=\"Calibration Curve\", use_column_width=True)\n",
    "\n",
    "st.subheader('ROC Curve')\n",
    "st.image(\"./image/RF_ROC Curve.png\", caption=\"ROC Curve\", use_column_width=True)\n",
    "\n",
    "# 설명 추가\n",
    "st.markdown('''\n",
    "### 결과 해석\n",
    "1. **모델 성능 분석**:\n",
    "- 혼동 행렬(Confusion Matrix)을 보면:\n",
    "    - 진짜 음성(TN): 565건 (이탈하지 않을 것으로 예측했고 실제로 이탈하지 않음)\n",
    "    - 거짓 양성(FP): 33건 (이탈할 것으로 예측했으나 실제로 이탈하지 않음)\n",
    "    - 거짓 음성(FN): 34건 (이탈하지 않을 것으로 예측했으나 실제로 이탈함)\n",
    "    - 진짜 양성(TP): 168건 (이탈할 것으로 예측했고 실제로 이탈함)\n",
    "\n",
    "- 모델 성능 지표:\n",
    "    - 정확도 91.63%: 전체 예측 중 약 92%가 정확함\n",
    "    - 정밀도 83.58%: 이탈 예측 중 실제 이탈한 비율\n",
    "    - F1 점수 83.37%: 정밀도와 재현율의 조화평균으로 양호한 수준\n",
    "            \n",
    "2. **Calibration Curve 분석**:\n",
    "- 모델의 예측이 잘 보정(calibrated)되었음을 나타내며, 예측 확률이 높을수록 실제 양성 비율도 증가\n",
    "- 그래프가 대각선(Perfectly Calibrated)에 가까울수록 모델의 예측이 신뢰할 수 있음을 의미\n",
    "- 이 경우, 모델의 예측이 비교적 잘 보정되어 있지만, 예측 확률이 0.5 이하일 때와 0.9 이상일 때 실제 양성 비율이 다소 떨어지는 경향이 있다. 이는 특정 구간에서 모델의 신뢰도를 향상시킬 여지가 있음을 시사.            \n",
    "\n",
    "3. **ROC 곡선 및 AUC 분석**:\n",
    "- ROC 곡선은 모델이 양성과 음성을 잘 구분하고 있음. (곡선이 왼쪽 위 코너에 가까워질수록 모델의 성능이 우수함)\n",
    "- AUC 값이 0.96으로 매우 높아, 모델이 96%의 확률로 양성과 음성을 구분할 수 있음을 보여줌. -> 모델의 분류 성능이 뛰어나며 신뢰할 수 있는 예측을 제공한다는 것을 의미.\n",
    "\n",
    "#### **최종 결론**:\n",
    "- 모델의 예측 성능이 전반적으로 우수하며, 특히 91.63%의 높은 정확도를 보임\n",
    "- ROC 곡선과 AUC 분석 결과, 모델의 분류 성능이 매우 뛰어나며, 신뢰할 수 있는 예측을 제공함     \n",
    "\n",
    "''')\n",
    "\n",
    "st.write(\"더 자세한 내용은 깃허브를 통해 확인하세요!\")\n",
    "st.markdown(\"[메인페이지로 가기](./app.py)\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "pystudy_env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
