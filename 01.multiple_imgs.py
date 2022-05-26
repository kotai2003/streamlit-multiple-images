# https://cafe-mickey.com/python/streamlit-5/
# https://discuss.streamlit.io/t/grid-of-images-with-the-same-height/10668/7
import streamlit as st
import os

st.title('Multiple Images')

#絶対パスを取得
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
print(PROJECT_PATH)

#画像保存フォルダのパスを取得
image_dir = os.path.join(PROJECT_PATH,'images')
print(image_dir)

# 画像ファイルのリストを取得
fName_list = os.listdir(image_dir)

#画像ファイル数
print(len(os.listdir(image_dir)))
img_file_num = len(os.listdir(image_dir))

#multiple images　Grid表示

idx = 0

for _ in range(len(fName_list)-1):
    cols = st.columns(4)

    if idx < len(fName_list):
        cols[0].image(f'./images/{fName_list[idx]}',width=150, caption=fName_list[idx])
        print(os.path.join(image_dir, fName_list[idx]))
        idx += 1
    if idx < len(fName_list):
        cols[1].image(f'./images/{fName_list[idx]}',width=150, caption=fName_list[idx])
        idx += 1
    if idx < len(fName_list):
        cols[2].image(f'./images/{fName_list[idx]}',width=150, caption=fName_list[idx])
        idx += 1
    if idx < len(fName_list):
        cols[3].image(f'./images/{fName_list[idx]}',width=150, caption=fName_list[idx])
        idx += 1
    else:
        break








