import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import japanize_matplotlib
import plotly.express as px

# Excelファイルを読み込む
# df = pd.read_excel('data/demo_data_v1.xlsx')
df_address = pd.read_excel("data/demo_data_v3.xlsx")

st.title('メディカルサーチ (患者様)')
region = st.selectbox(
    '都道府県: ',
    ["東京都"])
# hospital_name = st.text_input('病院名：')
symptom = st.selectbox(
    "症状: ",
    df_address["症状の例"].unique())
button_pressed = st.button(label='検索')
# 件数が大きい順番に並び替える
# filtered_df = df[(df["施設名"] == hospital_name) & (df["症状"] == disease_name)]
# filtered_df_address = df_address[(df_address["施設名"] == hospital_name) & (
#    df_address["症状"] == disease_name)]

filtered_df_address = df_address[
    (df_address["都道府県"] == region)
    & (df_address["症状の例"] == symptom)]

sorted = filtered_df_address.sort_values(by="件数", ascending=False)
num_surgeries = sorted.groupby('手術の有無')['件数'].sum().reset_index()
if button_pressed:
    st.subheader('検索結果', divider="blue")
    st.subheader(f"考えられる病気は {sorted['病名'].unique()[0]}")
    st.subheader(f"手術が必要な可能性 ")

    fig, ax = plt.subplots()
    ax.pie(num_surgeries["件数"], labels=num_surgeries["手術の有無"].unique(
    ), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    st.subheader(f"治療が受けられる病院（件数順）")
    fig = px.bar(sorted.reset_index().head(5).sort_values(by="件数", ascending=True), x="件数",
                 y="施設名", color="手術の有無", orientation="h")
    st.plotly_chart(fig, use_container_width=True)

    # 地図を表示
    st.map(sorted.head(5))
