import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Image to PDF Converter", page_icon="🖼️")

st.title("🖼️ Image to PDF Converter")
st.write("Upload multiple images and download them as a single PDF.")

# Upload images
uploaded_images = st.file_uploader(
    "Choose images (JPEG/PNG)", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

if uploaded_images:
    # Convert uploaded images to PIL and ensure RGB mode
    image_list = []
    for img_file in uploaded_images:
        image = Image.open(img_file).convert("RGB")
        image_list.append(image)

    # Button to generate PDF
    if st.button("Convert to PDF"):
        if image_list:
            # Save PDF to memory
            pdf_bytes = io.BytesIO()
            image_list[0].save(pdf_bytes, format="PDF", save_all=True, append_images=image_list[1:])
            pdf_bytes.seek(0)

            # Offer download
            st.success("PDF created successfully!")
            st.download_button(
                label="📥 Download PDF",
                data=pdf_bytes,
                file_name="converted.pdf",
                mime="application/pdf"
            )
        else:
            st.error("No valid images to convert.")
