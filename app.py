import streamlit as st
from PIL import Image
import io

# Import the function from caption_generator.py
from caption_generator import generate_caption  

st.title("🖼️ Image Caption Generator")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the uploaded file to a format that generate_caption() can process
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=image.format)

    # Generate caption on button click
    if st.button("Generate Caption"):
        try:
            caption = generate_caption(image_bytes)  # Pass image bytes instead of file path
            st.subheader("Generated Caption:")
            st.write(caption)
        except Exception as e:
            st.error(f"Error generating caption: {e}")
