import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Wallet", page_icon=":heavy_dollar_sign:", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv('online_action.csv')
    return data


def main():
    data = load_data()

    with st.container():
        left_column, center_column, right_column = st.columns([1, 8, 1])
        center_column.title('💲 B3 Stock Market - Updated data 💲')
        with center_column:
            st.dataframe(data, hide_index=True)

    with st.expander("Click to share images"):
        l_column, c_column, r_column = st.columns([2, 0.5, 2])
        l_column.image("cs50P.jpg")
        r_column.image("shirtificate.png")


if __name__ == '__main__':
    main()
