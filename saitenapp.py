import streamlit as st
from PIL import Image
import pandas as pd
import openpyxl

st.title('採点サービス　ログイン者数推移')
st.caption('★採点サービスのログイン者数の推移グラフです。2025年1月24日(金)～稼働。')

# 画像表示
image = Image.open('mec_saiten.jpg')
st.image(image, width=250)

# 年度選択メニュー（サイドバー）
year = st.sidebar.selectbox("年度を選択してください", ["2025", "2024"])

# 選択された年度に応じたCSVファイルを読み込む
csv_file = f"saiten_{year}.csv"
try:
    df = pd.read_csv(csv_file, index_col='日')
    st.line_chart(df)
    sort_df = df.sort_values(by="日", ascending=False)
    st.dataframe(sort_df.style.highlight_max(axis=0), height=200)
except FileNotFoundError:
    st.error(f"{csv_file} が見つかりません。該当年度のデータが存在しない可能性があります。")

# 大学別入力状況
st.caption('★採点サービスの大学別の入力状況です。2025年3月14日 AM 9:00 時点')
df2 = pd.read_excel('saitenuni.xlsx', index_col='大学', dtype='object', engine='openpyxl')
st.dataframe(df2, width=600, height=3250)
