import streamlit as st
import numpy as np
import pandas as pd


st.title('メディカルサーチ')
hospital_name = st.text_input('病院名：')
disease_name = st.text_input('病名：')
symptom = st.text_input("症状: ")
st.button(label='検索')

# Excelファイルを読み込む
df = pd.read_excel('data/demo_data_v1.xlsx')

# 件数が大きい順番に並び替える
filtered_df = df[(df["施設名"] == hospital_name) & (df["症状"] == disease_name)]
sorted = filtered_df.sort_values(by="件数", ascending=False)

# テーブルを表示
st.table(sorted)

# TODO: n件数のバープロットを表示
# st.subheader('折れ線グラフ')
# chart_data = pd.DataFrame(
#      np.random.randn(7, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)
# st.dataframe(chart_data)

# 地図を表示
# st.map(sorted, "緯度", "経度", size="件数")
