import streamlit as st

from ui.eda import run_eda
from ui.home import run_home
from ui.ml import run_ml


def main():
        st.markdown("""
        <style>
            .title {
                position: absolute;
                top: 10px;
                left: 10px;
                font-size: 30px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title displayed at top left corner
        st.markdown('<div class="title">자동차 가격 예측 앱</div>', unsafe_allow_html=True)

        menu = ['Home', 'EDA', 'ML']
        choice = st.sidebar.selectbox('메뉴', menu )

        if choice == menu[0] :
            run_home()
        elif choice == menu[1]:
            run_eda()    
        elif choice == menu[2]:
            run_ml()        





if __name__ == '__main__':
    main()