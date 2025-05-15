import pandas as pd
import img2pdf
from PIL import Image, ImageEnhance, ImageOps
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

def excel_to_image(excel_file, output_image):
    df = pd.read_excel(excel_file)
    fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

    font_path = "malgun.ttf"  # 또는 나눔고딕 TTF
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

    plt.savefig(output_image, dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.close()

def apply_black_white_filter(input_image, output_bw_image):
    img = Image.open(input_image).convert('L')
    img = ImageOps.autocontrast(img)
    img = ImageEnhance.Contrast(img).enhance(1.8)
    img.save(output_bw_image)

def image_to_pdf(input_bw_image, output_pdf):
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(input_bw_image))

def excel_to_scanlike_pdf(excel_file, output_pdf):
    temp_image = "temp_excel_render.png"
    temp_bw_image = "temp_excel_bw.png"

    excel_to_image(excel_file, temp_image)
    apply_black_white_filter(temp_image, temp_bw_image)
    image_to_pdf(temp_bw_image, output_pdf)

    os.remove(temp_image)
    os.remove(temp_bw_image)
