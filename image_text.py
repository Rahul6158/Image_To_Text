import streamlit as st
from PIL import Image
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def main():
    st.title("Text Extraction from Image with Streamlit")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Text"):
            text = ocr_core(image)
            st.subheader("Extracted Text:")
            st.write(text)

if __name__ == "__main__":
    main()
