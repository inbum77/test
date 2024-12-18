import streamlit as st
import fitz  # PyMuPDF
from pptx import Presentation
from pptx.util import Inches
import io
from PIL import Image

# PDF를 이미지로 변환하는 함수
def pdf_to_images(pdf_bytes):
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    images = []
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    return images

# 이미지 리스트를 PPTX로 변환하는 함수
def images_to_pptx(images):
    prs = Presentation()
    
    for img in images:
        slide = prs.slides.add_slide(prs.slide_layouts[5])  # 빈 슬라이드 레이아웃

        # 이미지의 크기를 인치로 변환
        width, height = img.size
        width_in_inches = width / 96
        height_in_inches = height / 96

        # 이미지 저장을 위해 BytesIO 사용
        image_stream = io.BytesIO()
        img.save(image_stream, format="PNG")
        image_stream.seek(0)

        # 슬라이드에 이미지 추가
        slide.shapes.add_picture(image_stream, Inches(0), Inches(0), width=Inches(width_in_inches), height=Inches(height_in_inches))

    return prs

# Streamlit UI
st.title("📄 PDF를 PPTX로 변환하기")
st.write("PDF 파일을 업로드하면 각 페이지를 이미지로 변환하여 PPTX 파일로 만들어줍니다. 😊")

upload
