import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Excelファイルを読み込む
# df = pd.read_excel('data/demo_data_v1.xlsx')
df_address = pd.read_excel("data/demo_data_v3.xlsx")

st.title('メディカルサーチ(医療関係者様)')
region = st.selectbox(
    '都道府県: ',
    ["東京都"])
# hospital_name = st.text_input('病院名：')
disease_name = st.selectbox(
    '病名: ',
    df_address.病名.unique())

# 型をボタンで指定できるようにする
# severity = st.selectbox(
#    '手術の有無:  ',
#    df_address["手術の有無"].unique())
button_pressed = st.button(label='検索')
# 件数が大きい順番に並び替える
# filtered_df = df[(df["施設名"] == hospital_name) & (df["症状"] == disease_name)]
# filtered_df_address = df_address[(df_address["施設名"] == hospital_name) & (
#    df_address["症状"] == disease_name)]

filtered_df_address = df_address[(
    df_address["病名"] == disease_name)
    & (df_address["都道府県"] == region)]

sorted = filtered_df_address.sort_values(by="件数", ascending=False)

if button_pressed:
    st.subheader('検索結果', divider="blue")
    fig = px.bar(sorted.reset_index().head(5).sort_values(by="件数", ascending=True), x="件数",
                 y="施設名", color="手術の有無", orientation="h")
    st.plotly_chart(fig, use_container_width=True)
    # 地図を表示
    st.map(sorted.head(5), size=20)
