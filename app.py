import streamlit as st

from ui.eda import run_eda
from ui.home import run_home
from ui.ml import run_ml

def main():
    # 사이드바를 먼저 생성
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    # 제목을 컨테이너 안에 넣어 왼쪽 정렬
    with st.container():
        st.markdown("<h1 style='text-align: left;'>자동차 가격 예측 앱</h1>", unsafe_allow_html=True)

    # 선택된 메뉴에 따라 해당 페이지 실행
    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()    
    elif choice == menu[2]:
        run_ml()        

if __name__ == '__main__':
    main()