import streamlit as st
import numpy as np
import pandas as pd

st.title('メディカルサーチ')
region = st.text_input('地域：')
symp = st.text_input('症状：')
distance = st.text_input('移動距離：')
st.button(label='検索')

# Excelファイルを読み込む
df = pd.read_excel('/Users/yukitajima/Documents/file/Book1.xlsx')

# キーワードを指定
keyword1 = region
keyword2 = symp

# キーワードを含む行を抽出
filtered_df = df[(df["区"] == keyword1) &(df["症状"] == keyword2)]
print(filtered_df)

# st.subheader('折れ線グラフ')
# chart_data = pd.DataFrame(
#      np.random.randn(7, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)
# st.dataframe(chart_data)

