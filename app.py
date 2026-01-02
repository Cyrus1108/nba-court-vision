import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="NBA COURT VISION",page_icon="🏀")

st.title("🏀 NBA COURT VISION")
st.write("DevOps Powered Player Comparison System")

st.sidebar.header("选择球员")
player1 = st.sidebar.text_input("球员1","LeBron James")
player2 = st.sidebar.text_input("球员2","Stephen Curry")

if st.button('开始对决（Analyst）'):
    st.subheader(f"{player1} VS {player2}")

    categories = ['得分','篮板','助攻','防守','效率']

    df = pd.DataFrame({
        '能力维度': categories,
        player1: np.random.randint(60, 100, 5),
        player2: np.random.randint(60, 100, 5)
    })

    st.table(df)

    st.line_chart(df.set_index('能力维度'))

    st.success("Analysis Complete！（Data is simulated for DevOps testing）")