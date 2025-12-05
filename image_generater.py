
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import io

st.title("64×64 お絵描きキャンバス")

# --- キャンバス設定 ---
canvas_width = 256   # 表示サイズ
canvas_height = 256

stroke_width = 12 #st.slider("ブラシサイズ", 1, 20, 10)

image_label = st.text_input("画像ラベルを入力してください")

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 1)",
    stroke_width=stroke_width,
    stroke_color="#000000",
    background_color="#FFFFFF",
    width=canvas_width,
    height=canvas_height,
    drawing_mode="freedraw",
    key="canvas",
)

# --- 画像の生成とダウンロード ---
if canvas_result.image_data is not None:
    # Pillow形式に変換
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))

    # 保存用に 64x64 に縮小
    img_64 = img.resize((64, 64), Image.NEAREST)

    # BytesIO バッファに png として保存
    img_buffer = io.BytesIO()
    img_64.save(img_buffer, format="PNG")
    img_bytes = img_buffer.getvalue()

    # ダウンロードボタン
    st.download_button(
        label="画像をダウンロード（64×64 PNG）",
        data=img_bytes,
        file_name=f"{image_label}.png",
        mime="image/png"
    )

    #st.image(img_64, caption="保存される 64×64画像", width=256)
#else:
#    st.warning("キャンバスに描いてください")

