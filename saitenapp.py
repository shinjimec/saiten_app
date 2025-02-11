import streamlit as st
from PIL import Image
import pandas as pd
import openpyxl

st.title('採点サービス　ログイン者数推移')
st.caption('★採点サービスのログイン者数の推移グラフです。2025年1月24日(金)～稼働。')

# 画像
image = Image.open('mec_saiten.jpg')
st.image(image,width=250)

# データ分析
df = pd.read_csv('saiten.csv',index_col='日')
st.line_chart(df)
st.dataframe(df.style.highlight_max(axis=0), height=200)

st.caption('★採点サービスの大学別の入力状況です。2025年2月11日時点')
# データ分析
df2 = pd.read_excel('saitenuni.xlsx',index_col='大学', dtype='object')
st.dataframe(df2, width=600, height=3250)