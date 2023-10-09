import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Wallet", page_icon=":heavy_dollar_sign:", layout="wide")

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


@st.cache_data
def load_data():
    data = pd.read_csv('online_action.csv')
    return data


def main():
    data = load_data()

    st.header('Stock Status all in one')
    st.markdown("##")
    total1,total2,total3=st.columns(3,gap='large')

    with total1:
        st.metric(label="Number of Stocks", value=str(data.shape[0]))

    with total2:
        st.metric(label="Most expensive stock", value=str(data["CURRENT VALUE (R$)"].max()))

    with total3:
        st.metric(label="Cheapest stock", value=str(data["CURRENT VALUE (R$)"].min()))

    with st.container():
        left_column, center_column, right_column = st.columns([1, 8, 1])
        center_column.title('💲 B3 Stock Market - Updated data 💲')
        
        with center_column:
            st.dataframe(data, hide_index=True)

    with st.expander("CS50's Introduction to Programming with Python"):
        l_column, c_column, r_column = st.columns([1.5, 1.5, 1.5])
        l_column.image("cs50P.jpg")
        c_column.image("harvard.png")
        r_column.image("shirtificate.png")


if __name__ == '__main__':
    main()
