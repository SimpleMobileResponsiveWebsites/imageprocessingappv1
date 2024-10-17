import streamlit as st
from PIL import Image
import numpy as np

def main():
    st.title("Image Processing App")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)

        # Display original image
        st.subheader("Original Image")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Image processing options
        st.subheader("Image Processing")
        option = st.selectbox(
            'Choose an image processing option:',
            ('None', 'Grayscale', 'Invert Colors', 'Increase Brightness')
        )

        if option == 'Grayscale':
            processed_image = image.convert('L')
            st.image(processed_image, caption="Grayscale Image", use_column_width=True)
        
        elif option == 'Invert Colors':
            processed_image = Image.eval(image, lambda x: 255 - x)
            st.image(processed_image, caption="Inverted Image", use_column_width=True)
        
        elif option == 'Increase Brightness':
            brightness_factor = st.slider("Brightness factor", 1.0, 3.0, 1.5)
            processed_image = Image.eval(image, lambda x: min(int(x * brightness_factor), 255))
            st.image(processed_image, caption=f"Brightened Image (factor: {brightness_factor})", use_column_width=True)

if __name__ == "__main__":
    main()
