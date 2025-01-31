import streamlit as st
from PIL import Image
import pandas as pd

st.title('採点サービス　ログイン者数推移')
st.caption('これは採点サービスのログイン者数の推移グラフです。2025年1月24日(金)～稼働。')

# 画像
image = Image.open('mec_saiten.jpg')
st.image(image,width=250)

# データ分析
df = pd.read_csv('saiten.csv',index_col='日')
st.line_chart(df)
st.dataframe(df)