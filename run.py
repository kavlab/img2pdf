import streamlit as st
import img2pdf

images = []

uploaded_files = st.file_uploader(
    "Загрузка изображений",
    accept_multiple_files=True,
    type=['jpg', 'png']
)

if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        images.append(uploaded_file.read())

    if images:
        st.download_button(
            label='Загрузить PDF',
            data=img2pdf.convert(images),
            file_name='output.pdf',
            mime='application/pdf'
        )
else:
    images = []
