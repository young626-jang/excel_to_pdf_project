import streamlit as st
import os
from excel_to_pdf_utils import excel_to_scanlike_pdf

st.title("엑셀 → 흑백 스캔 스타일 PDF 변환기 🖤")
uploaded_file = st.file_uploader("엑셀 파일 업로드", type=["xlsx", "xls"])

if uploaded_file is not None:
    output_pdf = "converted_scan_style.pdf"
    with open("uploaded.xlsx", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("변환 시작"):
        try:
            excel_to_scanlike_pdf("uploaded.xlsx", output_pdf)
            with open(output_pdf, "rb") as f:
                st.download_button("흑백 PDF 다운로드", f, file_name="scan_style_output.pdf")
            os.remove("uploaded.xlsx")
            os.remove(output_pdf)
        except Exception as e:
            st.error(f"오류 발생: {e}")
