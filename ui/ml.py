import streamlit as st
import joblib
import numpy as np

def run_ml():

    # 유저에게 예측에 필요한 데이터를 입력받는다.
    # 나이, 연봉, 신용카드 부채, 순자산 을 입력받는다.
    # 인공지능으로 예측하여, 결과를 화면에 보여준다.

    st.subheader('자동차 가격 예측')
    st.text('사용자의 정보를 입력하세요.')
    age = st.number_input('나이', min_value=18, max_value=120, value=30)
    salary = st.number_input('연봉', min_value=1000, value=10000)
    debt = st.number_input('신용카드 부채', min_value=0, value=10000)
    worth = st.number_input('순자산', min_value=1000, value=30000)

    # 학습할 때 describe보고 최소,최대값 보고 만든다.
    if st.button('구매 금액 예측하기') :
        regressor = joblib.load('model/regressor.pk1')
        new_data = np.array( [age, salary, debt, worth] ).reshape(1,4)
        y_pred = regressor.predict(new_data)

        pred_data = y_pred[0]

        if pred_data <0 :
            st.error('예측이 불가능한 데이터 입니다.')
        else: 
            # 정수부분만 보여주자.(소수점 버리기)
            pred_data = round(pred_data)
            # 숫자에 3자리마다, 콤마를 찍어주기
            pred_data = format(pred_data, ',')
            print(type(pred_data))
            st.success(f'예측 금액은 {pred_data} 달라 입니다.')    

        
    





