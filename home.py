import streamlit as st
import numpy as np
import pandas as pd


# Excelファイルを読み込む
# df = pd.read_excel('data/demo_data_v1.xlsx')
df_address = pd.read_excel("data/demo_data_v2.xlsx")

st.title('メディカルサーチ')
region = st.selectbox(
    '都道府県: ',
    ["東京都"])
# hospital_name = st.text_input('病院名：')
disease_name = st.selectbox(
    '病名: ',
    df_address.症状.unique())
symptom = st.text_input("症状: ")

# 型をボタンで指定できるようにする
# 症状
severity = st.selectbox(
    '手術の有無:  ',
    df_address["手術の有無"].unique())
button_pressed = st.button(label='検索')
# 件数が大きい順番に並び替える
# filtered_df = df[(df["施設名"] == hospital_name) & (df["症状"] == disease_name)]
# filtered_df_address = df_address[(df_address["施設名"] == hospital_name) & (
#    df_address["症状"] == disease_name)]

filtered_df_address = df_address[(
    df_address["症状"] == disease_name) & (df_address["都道府県"] == region) & (df_address["手術の有無"] == severity)]
sorted = filtered_df_address.sort_values(by="件数", ascending=False)

if button_pressed:
    # テーブルを表示
    st.table(sorted[["都道府県", "区", "施設名", "手術の有無", "件数"]].head(5))

# TODO: n件数のバープロットを表示
# st.subheader('折れ線グラフ')
# chart_data = pd.DataFrame(
#      np.random.randn(7, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)
# st.dataframe(chart_data)

    # 地図を表示
    st.map(sorted.head(5), size=20)
